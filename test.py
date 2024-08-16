import numpy as np
import matplotlib.pyplot as plt

# パラメータ設定
mass = 1.0       # 質量 (kg)
k = 1.0          # バネ定数 (N/m)
omega = np.sqrt(k / mass)  # 角振動数 (rad/s)
A = 1.0          # 振幅 (m)
phi = 0          # 初期位相 (rad)
t = np.linspace(0, 10, 1000)  # 時間 (秒)

# 単振動の位置を計算
x = A * np.cos(omega * t + phi)

# 散布図としてプロット
plt.figure(figsize=(8, 4))
plt.scatter(t, x, color='blue', s=10, label='Simple Harmonic Motion')
plt.title('Simple Harmonic Motion Simulation')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.legend()
plt.grid(True)
plt.show()