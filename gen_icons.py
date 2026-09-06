import os
from PIL import Image, ImageDraw, ImageFont

def create_app_icon(size, filename):
    # Create image with RGBA
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Rounded background with smooth gradient or solid dark surface with gradient effect
    radius = int(size * 0.22)
    
    # Background box
    # Outer rounded rectangle
    draw.rounded_rectangle(
        [(0, 0), (size, size)],
        radius=radius,
        fill=(22, 27, 34, 255),
        outline=(88, 166, 255, 180),
        width=max(2, int(size * 0.02))
    )
    
    # Inner badge background
    inner_pad = int(size * 0.15)
    draw.rounded_rectangle(
        [(inner_pad, inner_pad), (size - inner_pad, size - inner_pad)],
        radius=int(radius * 0.7),
        fill=(33, 38, 45, 255),
        outline=(188, 140, 255, 120),
        width=max(1, int(size * 0.015))
    )
    
    # Draw an isometric stylized inventory box
    cx, cy = size // 2, size // 2
    box_w = int(size * 0.42)
    box_h = int(size * 0.38)
    
    # Top face
    top_face = [
        (cx, cy - box_h // 2),
        (cx + box_w // 2, cy - box_h // 4),
        (cx, cy),
        (cx - box_w // 2, cy - box_h // 4)
    ]
    draw.polygon(top_face, fill=(88, 166, 255, 255), outline=(230, 237, 243, 220))
    
    # Left face
    left_face = [
        (cx - box_w // 2, cy - box_h // 4),
        (cx, cy),
        (cx, cy + box_h // 2),
        (cx - box_w // 2, cy + box_h // 4)
    ]
    draw.polygon(left_face, fill=(40, 100, 200, 255), outline=(230, 237, 243, 180))
    
    # Right face
    right_face = [
        (cx, cy),
        (cx + box_w // 2, cy - box_h // 4),
        (cx + box_w // 2, cy + box_h // 4),
        (cx, cy + box_h // 2)
    ]
    draw.polygon(right_face, fill=(188, 140, 255, 255), outline=(230, 237, 243, 180))
    
    # Center fold tape line
    tape_top = [(cx, cy - box_h // 2), (cx, cy)]
    draw.line(tape_top, fill=(240, 180, 50, 255), width=max(2, int(size * 0.03)))
    
    # Green upward indicator dot (signifying stock tracking)
    dot_radius = int(size * 0.06)
    dot_cx = int(size * 0.78)
    dot_cy = int(size * 0.24)
    draw.ellipse(
        [(dot_cx - dot_radius, dot_cy - dot_radius), (dot_cx + dot_radius, dot_cy + dot_radius)],
        fill=(63, 185, 80, 255),
        outline=(255, 255, 255, 200),
        width=max(1, int(size * 0.015))
    )
    
    target_dir = r"C:\Users\LNM Group 6\.gemini\antigravity\scratch\stock-tracker"
    img.save(os.path.join(target_dir, filename), "PNG")
    print(f"Generated {filename} ({size}x{size})")

create_app_icon(192, "icon-192.png")
create_app_icon(512, "icon-512.png")
create_app_icon(180, "apple-touch-icon.png")
