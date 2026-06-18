import asyncio
import time
import random
import json
import os
import httpx

# Configuration
BASE_URL = os.environ.get("REACT_APP_BACKEND_URL", "http://localhost:8000").rstrip("/")
API_URL = f"{BASE_URL}/api"
CONCURRENT_USERS = 100
TEST_DURATION_SECS = 60
THINK_TIME_MIN = 0.05
THINK_TIME_MAX = 0.2

# Test Account Credentials (must match existing backend_test.py credentials or be created)
TEST_EMAIL = "test.user.krinterior@example.com"
TEST_PASSWORD = "Test@123456"
TEST_FULL_NAME = "Test Load User"

async def ensure_test_user_exists():
    """Sign up the test user if not exists, or log in to verify credentials."""
    print(f"Verifying target backend at {API_URL}...")
    async with httpx.AsyncClient(timeout=10) as client:
        # Check root
        try:
            r = await client.get(f"{API_URL}/")
            if r.status_code != 200:
                print(f"Backend root check returned status {r.status_code}. Content: {r.text}")
        except Exception as e:
            print(f"Error connecting to backend: {e}")
            print("Please make sure the backend server is running on http://localhost:8000")
            return None

        # Try logging in
        login_payload = {"email": TEST_EMAIL, "password": TEST_PASSWORD}
        r = await client.post(f"{API_URL}/auth/login", json=login_payload)
        if r.status_code == 200:
            print("Test user login verified.")
            return r.json()["access_token"]
        
        # If login fails, try signing up
        print("Login failed, attempting to register test user...")
        signup_payload = {"email": TEST_EMAIL, "password": TEST_PASSWORD, "full_name": TEST_FULL_NAME}
        r = await client.post(f"{API_URL}/auth/signup", json=signup_payload)
        if r.status_code == 200:
            print("Test user successfully registered.")
            return r.json()["access_token"]
        elif r.status_code == 400 and "already" in r.text.lower():
            # Should not happen since login failed, but handle just in case
            print("User already exists but verification failed (check credentials).")
        
        print(f"Could not verify test user credentials: {r.status_code} {r.text}")
        return None

async def worker(worker_id, token, duration, results):
    """Simulates a single virtual user session making requests for the duration."""
    start_time = time.time()
    end_time = start_time + duration
    
    headers = {
        "Content-Type": "application/json"
    }
    auth_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    } if token else headers

    # Define tasks with relative probabilities
    # 0: Root (Public) - 40%
    # 1: Profile (Authenticated) - 30%
    # 2: Projects List (Authenticated) - 20%
    # 3: Login (Public - Hashing overhead) - 10%
    
    endpoints = [
        {"name": "Root", "method": "GET", "url": f"{API_URL}/", "auth": False},
        {"name": "Profile", "method": "GET", "url": f"{API_URL}/auth/me", "auth": True},
        {"name": "List Projects", "method": "GET", "url": f"{API_URL}/projects", "auth": True},
        {"name": "Login", "method": "POST", "url": f"{API_URL}/auth/login", "auth": False, "json": {"email": TEST_EMAIL, "password": TEST_PASSWORD}}
    ]
    weights = [0.40, 0.30, 0.20, 0.10]

    async with httpx.AsyncClient(timeout=15) as client:
        while time.time() < end_time:
            # Pick a task based on weights
            task = random.choices(endpoints, weights=weights, k=1)[0]
            
            # Use appropriate headers
            req_headers = auth_headers if task["auth"] else headers
            
            req_start = time.time()
            status_code = 0
            success = False
            
            try:
                if task["method"] == "GET":
                    r = await client.get(task["url"], headers=req_headers)
                elif task["method"] == "POST":
                    r = await client.post(task["url"], headers=req_headers, json=task.get("json"))
                else:
                    r = None
                
                if r:
                    status_code = r.status_code
                    # Standard FastAPI success codes are 200
                    success = (status_code == 200)
            except httpx.RequestError as e:
                # Network or connection errors
                status_code = 0
                success = False
            
            req_end = time.time()
            latency = (req_end - req_start) * 1000.0 # in milliseconds
            
            # Record result
            results.append({
                "timestamp": req_start,
                "endpoint": task["name"],
                "status_code": status_code,
                "latency_ms": latency,
                "success": success
            })
            
            # Think time (simulates user reading page, typing, clicking)
            await asyncio.sleep(random.uniform(THINK_TIME_MIN, THINK_TIME_MAX))

def analyze_results(raw_results, duration):
    """Computes stats from raw test data."""
    total_reqs = len(raw_results)
    if total_reqs == 0:
        return {}

    successful_reqs = sum(1 for r in raw_results if r["success"])
    failed_reqs = total_reqs - successful_reqs
    success_rate = (successful_reqs / total_reqs) * 100.0
    average_rps = total_reqs / duration

    # Group results by endpoint
    endpoint_data = {}
    for r in raw_results:
        ep = r["endpoint"]
        if ep not in endpoint_data:
            endpoint_data[ep] = []
        endpoint_data[ep].append(r)

    endpoint_stats = {}
    for ep, reqs in endpoint_data.items():
        ep_total = len(reqs)
        ep_success = sum(1 for r in reqs if r["success"])
        ep_failed = ep_total - ep_success
        ep_success_rate = (ep_success / ep_total) * 100.0
        
        latencies = sorted([r["latency_ms"] for r in reqs])
        
        avg_latency = sum(latencies) / ep_total if ep_total > 0 else 0
        min_latency = latencies[0] if ep_total > 0 else 0
        max_latency = latencies[-1] if ep_total > 0 else 0
        
        # Percentiles
        p90_idx = int(ep_total * 0.90)
        p95_idx = int(ep_total * 0.95)
        
        p90_latency = latencies[p90_idx] if ep_total > p90_idx else latencies[-1]
        p95_latency = latencies[p95_idx] if ep_total > p95_idx else latencies[-1]
        
        endpoint_stats[ep] = {
            "total_requests": ep_total,
            "successful_requests": ep_success,
            "failed_requests": ep_failed,
            "success_rate": ep_success_rate,
            "avg_response_time_ms": avg_latency,
            "min_response_time_ms": min_latency,
            "max_response_time_ms": max_latency,
            "p90_response_time_ms": p90_latency,
            "p95_response_time_ms": p95_latency,
            "rps": ep_total / duration
        }

    # Global latencies
    all_latencies = sorted([r["latency_ms"] for r in raw_results])
    global_avg_latency = sum(all_latencies) / total_reqs
    global_min_latency = all_latencies[0]
    global_max_latency = all_latencies[-1]
    
    p90_idx = int(total_reqs * 0.90)
    p95_idx = int(total_reqs * 0.95)
    global_p90 = all_latencies[p90_idx] if total_reqs > p90_idx else all_latencies[-1]
    global_p95 = all_latencies[p95_idx] if total_reqs > p95_idx else all_latencies[-1]

    return {
        "summary": {
            "concurrent_users": CONCURRENT_USERS,
            "test_duration_seconds": duration,
            "total_requests": total_reqs,
            "successful_requests": successful_reqs,
            "failed_requests": failed_reqs,
            "success_rate": success_rate,
            "average_rps": average_rps,
            "avg_response_time_ms": global_avg_latency,
            "min_response_time_ms": global_min_latency,
            "max_response_time_ms": global_max_latency,
            "p90_response_time_ms": global_p90,
            "p95_response_time_ms": global_p95
        },
        "endpoints": endpoint_stats
    }

async def main():
    print("=" * 60)
    print("         KRINTERIOR AI - BASELINE LOAD TESTING")
    print("=" * 60)
    print(f"Target URL: {BASE_URL}")
    print(f"Concurrent Users: {CONCURRENT_USERS}")
    print(f"Duration: {TEST_DURATION_SECS} seconds")
    print(f"Simulated Think Time: {THINK_TIME_MIN}s to {THINK_TIME_MAX}s")
    print("-" * 60)

    # 1. Authenticate user to obtain token
    token = await ensure_test_user_exists()
    if not token:
        print("Warning: Authenticated tests will fail. Running load test without auth token.")
    
    # 2. Run workers
    print(f"Spawning {CONCURRENT_USERS} concurrent workers...")
    raw_results = []
    
    start_time = time.time()
    
    # Create tasks
    workers = [
        worker(i, token, TEST_DURATION_SECS, raw_results)
        for i in range(CONCURRENT_USERS)
    ]
    
    # Display progress while running
    progress_task = None
    async def display_progress():
        while time.time() - start_time < TEST_DURATION_SECS:
            await asyncio.sleep(5)
            elapsed = time.time() - start_time
            reqs = len(raw_results)
            rps = reqs / elapsed if elapsed > 0 else 0
            print(f"Progress: {elapsed:.1f}s / {TEST_DURATION_SECS}s elapsed | {reqs} requests sent | Average RPS: {rps:.1f}")

    progress_task = asyncio.create_task(display_progress())
    
    # Run all workers in parallel
    await asyncio.gather(*workers)
    
    actual_duration = time.time() - start_time
    print(f"Load test finished. Run time: {actual_duration:.2f} seconds.")
    
    if progress_task:
        progress_task.cancel()
        try:
            await progress_task
        except asyncio.CancelledError:
            pass

    # 3. Analyze and save results
    print("Analyzing metrics...")
    stats = analyze_results(raw_results, actual_duration)
    
    # Add raw results to the output JSON
    stats["raw_results"] = raw_results
    
    # Ensure test_reports directory exists
    os.makedirs("test_reports", exist_ok=True)
    
    output_path = "test_reports/load_test_results.json"
    with open(output_path, "w") as f:
        json.dump(stats, f, indent=2)
        
    print(f"Saved load test metrics with {len(raw_results)} samples to: {os.path.abspath(output_path)}")
    print("-" * 60)
    
    s = stats["summary"]
    print("Summary:")
    print(f"  Total Requests:       {s['total_requests']}")
    print(f"  Success Rate:         {s['success_rate']:.2f}%")
    print(f"  Avg RPS:              {s['average_rps']:.2f} req/sec")
    print(f"  Avg Response Time:    {s['avg_response_time_ms']:.2f} ms")
    print(f"  Min/Max Response:     {s['min_response_time_ms']:.2f} ms / {s['max_response_time_ms']:.2f} ms")
    print(f"  p90/p95 Response:     {s['p90_response_time_ms']:.2f} ms / {s['p95_response_time_ms']:.2f} ms")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(main())
