import pypresence
import psutil
import time
import json

with open("config.json") as f:
    config = json.load(f)
RPC = pypresence.Presence(829135546538000384)
RPC.connect()
print("Discord Rich Presenceに接続しました。")

def get_readable_size(size):
    abs_size = abs(size)
    for suffix in ['B', 'KB', 'MB', 'GB', 'TB']:
        if abs_size < 1024:
            return f'{abs_size:3.2f} {suffix}'
        abs_size /= 1024

try:
    if config['mode'] == "adv":
        while True:
            memory = psutil.virtual_memory()
            RPC.update(
                state=f"CPU:{psutil.cpu_percent()}% Threads:{psutil.cpu_count()}",
                details=f"MEMORY:{memory.percent}% Total:{get_readable_size(memory.total)}",
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