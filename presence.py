import pypresence
import psutil
import time
import json

with open("config.json") as f:
    config = json.load(f)
RPC = pypresence.Presence(829135546538000384)
RPC.connect()
print("Discord Rich Presenceに接続しました。")
try:
    if config['mode'] == "adv":
        while True:
            memory = psutil.virtual_memory()
            RPC.update(
                state=f"CPU:{psutil.cpu_percent()}% Threads:{psutil.cpu_count()}",
                details=f"MEMORY:{memory.percent}% Total:{memory.total}KB",
                large_image="meter",
                large_text="Hardware_status"
                )
            time.sleep(3)
    elif config['mode'] == "normal":
            memory = psutil.virtual_memory()
            RPC.update(
                state=f"CPU:{psutil.cpu_percent()}%",
                details=f"MEMORY:{memory.percent}%",
                large_image="meter",
                large_text="Hardware_status"
                )
            time.sleep(3)
except KeyboardInterrupt:
    RPC.close()
    print("Discord Rich Presenceから切断しました。")
    exit()