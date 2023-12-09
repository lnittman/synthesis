from psutil import process_iter

def format_time(time: float) -> str:
    minutes = int(time // 60)
    seconds = int(time % 60)

    return f"{minutes:02d}:{seconds:02d}"

def kill_process_by_port(port):
    for proc in process_iter(['pid', 'name', 'connections']):
        if proc.info['connections']:
            for conn in proc.info['connections']:
                if conn.laddr.port == port:
                    print(f"Killing process {proc.info['pid']} using port {port}")
                    proc.kill()
                    break

