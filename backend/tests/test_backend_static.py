from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SERVER = ROOT / "server.py"


def test_backend_server_declares_expected_security_routes():
    source = SERVER.read_text(encoding="utf-8")
    for route in (
        '@api.post("/auth/signup"',
        '@api.post("/auth/login"',
        '@api.get("/auth/me"',
        '@api.post("/auth/logout"',
        '@api.get("/projects"',
        '@api.post("/design/generate"',
    ):
        assert route in source


def test_backend_uses_environment_for_secrets():
    source = SERVER.read_text(encoding="utf-8")
    assert 'os.environ["JWT_SECRET"]' in source
    assert 'os.environ["EMERGENT_LLM_KEY"]' in source
    assert "allow_credentials=True" in source
