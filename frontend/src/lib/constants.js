export const ROOM_TYPES = [
  { id: "Living Room", label: "Living Room", img: "https://images.unsplash.com/photo-1672860044506-e3ec09653e82?auto=format&fit=crop&w=600&q=70" },
  { id: "Bedroom", label: "Bedroom", img: "https://images.pexels.com/photos/13722870/pexels-photo-13722870.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=500&w=600" },
  { id: "Kitchen", label: "Kitchen", img: "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?auto=format&fit=crop&w=600&q=70" },
  { id: "Dining Room", label: "Dining Room", img: "https://images.unsplash.com/photo-1690489965043-ec15758cce71?auto=format&fit=crop&w=600&q=70" },
  { id: "Study Room", label: "Study Room", img: "https://images.unsplash.com/photo-1593476550610-87baa860004a?auto=format&fit=crop&w=600&q=70" },
  { id: "Home Office", label: "Home Office", img: "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=600&q=70" },
  { id: "Kids Room", label: "Kids Room", img: "https://images.unsplash.com/photo-1617325247661-675ab4b64ae2?auto=format&fit=crop&w=600&q=70" },
  { id: "Home Theater", label: "Home Theater", img: "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?auto=format&fit=crop&w=600&q=70" },
  { id: "Luxury Villa Hall", label: "Villa Hall", img: "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=600&q=70" },
];

export const BUDGET_PRESETS = [
  { label: "₹50K", value: 50000 },
  { label: "₹1L", value: 100000 },
  { label: "₹2L", value: 200000 },
  { label: "₹5L", value: 500000 },
  { label: "₹10L", value: 1000000 },
];

export const PALETTES = [
  { id: "Luxury Gold", colors: ["#C9A23D", "#F5E6BE", "#1A1208"] },
  { id: "Warm Beige", colors: ["#E5D3B3", "#C7A878", "#5A3E1B"] },
  { id: "Modern White", colors: ["#FFFFFF", "#F2F2F2", "#9DA1A8"] },
  { id: "Earth Brown", colors: ["#7A4A1F", "#C58A4E", "#F3D8B8"] },
  { id: "Royal Blue", colors: ["#0D2F66", "#3F6BB3", "#E1E9F5"] },
  { id: "Forest Green", colors: ["#1E4D2B", "#6D9E7A", "#E2EFE2"] },
  { id: "Minimal Grey", colors: ["#2B2B2B", "#7D7D7D", "#E8E8E8"] },
  { id: "Black Luxury", colors: ["#0A0A0A", "#404040", "#D4AF37"] },
];

export function formatINR(n) {
  if (n === null || n === undefined) return "₹0";
  return "₹" + Number(n).toLocaleString("en-IN");
}
