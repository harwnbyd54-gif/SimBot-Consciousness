import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import cv2
import os

# Create assets directory if it doesn't exist
os.makedirs("assets", exist_ok=True)
print("Creating project illustrative assets...")

# ==========================================
# 1. GENERATE: Panpsychic Mind Map Image
# ==========================================
plt.figure(figsize=(10, 8))
np.random.seed(42)

# Generate Mock TSP Points & Objects
tsp_cities = np.random.rand(50, 2) * 500
robot_pos = np.array([250.0, 260.0])
obj_stable = np.array([100.0, 400.0])
obj_tense = np.array([280.0, 200.0])

# Plot Background Path
plt.scatter(tsp_cities[:, 0], tsp_cities[:, 1], color='gray', s=15, alpha=0.3)
plt.plot(tsp_cities[tsp_cities[:, 0].argsort()][:, 0], tsp_cities[tsp_cities[:, 0].argsort()][:, 1], color='gray', linestyle=':', alpha=0.2)

# Plot Robot and Influence Zone
influence_zone = plt.Circle(robot_pos, 120, color='blue', fill=True, alpha=0.08)
plt.gca().add_patch(influence_zone)
plt.scatter(robot_pos[0], robot_pos[1], color='blue', s=300, marker='*', zorder=5)
plt.text(robot_pos[0] + 12, robot_pos[1] + 12, "SimBot AI Engine", fontsize=10, weight='bold', color='blue')

# Plot Stable Object
plt.scatter(obj_stable[0], obj_stable[1], color='green', s=200, marker='o', zorder=4)
plt.text(obj_stable[0] + 12, obj_stable[1] - 5, "Obj_1 (Stable)\nE: 100% | 🧘 Equilibrium", fontsize=9, color='green', weight='bold')

# Plot Tense Object (Within Radius)
plt.scatter(obj_tense[0], obj_tense[1], color='red', s=200, marker='X', zorder=4)
plt.text(obj_tense[0] + 12, obj_tense[1] - 5, "Obj_2 (Tense)\nE: 64.2% | ⚠️ High Tension", fontsize=9, color='red', weight='bold')
plt.plot([robot_pos[0], obj_tense[0]], [robot_pos[1], obj_tense[1]], 'r--', alpha=0.6, lw=1.5)

# Aesthetics
plt.title("Illustration 1: Panpsychic Spatial Stress Matrix Map", fontsize=12, pad=15, weight='bold')
plt.xlim(0, 500)
plt.ylim(0, 500)
plt.xlabel("X Coordinate (Spatial Mind Workspace)")
plt.ylabel("Y Coordinate (Spatial Mind Workspace)")
plt.grid(True, linestyle=':', alpha=0.5)

legend_elements = [
    Line2D([0], [0], marker='*', color='blue', label='SimBot AI Core', markersize=12, linestyle='None'),
    Line2D([0], [0], marker='o', color='green', label='Equilibrium Node', markersize=8, linestyle='None'),
    Line2D([0], [0], marker='X', color='red', label='High Tension Node', markersize=8, linestyle='None'),
    Line2D([0], [0], color='blue', alpha=0.15, lw=6, label='Robot Influence Field (R=120)')
]
plt.legend(handles=legend_elements, loc='upper right')
plt.savefig("assets/panpsychic_mind_map.png", dpi=150, bbox_inches='tight')
plt.close()
print("[✓] Saved: assets/panpsychic_mind_map.png")

# ==========================================
# 2. GENERATE: OpenCV Canny Edge Complexity Image
# ==========================================
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Generate Synthetic Geometry Image
mock_img = np.zeros((200, 200), dtype=np.uint8)
cv2.circle(mock_img, (60, 60), 30, 255, -1)
cv2.rectangle(mock_img, (110, 110), (170, 170), 255, -1)

# Apply Canny Edge Detection
edges = cv2.Canny(mock_img, 100, 200)

axes[0].imshow(mock_img, cmap='gray')
axes[0].set_title("Simulated RGB Camera Feed", fontsize=10, weight='bold')
axes[0].axis('off')

axes[1].imshow(edges, cmap='gray')
axes[1].set_title("Canny Edge Matrix Analysis", fontsize=10, weight='bold')
axes[1].axis('off')

plt.suptitle("Illustration 2: Real OpenCV Computer Vision Matrix Processing", fontsize=12, weight='bold', y=0.98)
plt.savefig("assets/opencv_vision_matrix.png", dpi=150, bbox_inches='tight')
plt.close()
print("[✓] Saved: assets/opencv_vision_matrix.png")

# ==========================================
# 3. GENERATE: Dual-Layer Auditory Signal Flow
# ==========================================
plt.figure(figsize=(10, 4))
time = np.linspace(0, 10, 500)

# Create baseline noise and an explicit anomaly sound spike
audio_signal = 15 * np.sin(2 * np.pi * 1 * time) + np.random.normal(0, 3, 500)
audio_signal[220:280] += 55 * np.sin(2 * np.pi * 5 * time[220:280]) # Severe anomaly spike

plt.plot(time, audio_signal, color='purple', alpha=0.7, lw=1.5, label='Decibel Field (dB)')
plt.axhline(y=40, color='orange', linestyle='--', alpha=0.8, lw=1.5, label='Listening Activation Threshold (40 dB)')

# Highlight regions
plt.fill_between(time, audio_signal, 40, where=(audio_signal > 40), color='red', alpha=0.3, label='Active Listening Engaged')
plt.fill_between(time, audio_signal, 40, where=(audio_signal <= 40), color='green', alpha=0.1, label='Passive Noise Suppression')

plt.title("Illustration 3: Dual-Layer Cognitive Auditory Loop Flowchart", fontsize=12, pad=12, weight='bold')
plt.xlabel("Time Vectors (Ticks)")
plt.ylabel("Sound Amplitude Intensity (dB)")
plt.ylim(-30, 90)
plt.grid(True, linestyle=':', alpha=0.5)
plt.legend(loc='upper right')

plt.savefig("assets/auditory_loop_flow.png", dpi=150, bbox_inches='tight')
plt.close()
print("[✓] Saved: assets/auditory_loop_flow.png")
print("\nSuccess! All visual assets are saved inside the 'assets/' folder.")
