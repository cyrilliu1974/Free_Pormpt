"""
Semantic Shortcuts — Streamlit launcher

Usage:
    python run_streamlit.py                 # default 0.0.0.0:8501
    python run_streamlit.py --port 8502
    python run_streamlit.py --host 127.0.0.1 --port 8501
"""
import argparse
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
APP = PROJECT_ROOT / "streamlit_app.py"


def main() -> int:
    parser = argparse.ArgumentParser(description="Launch Semantic Shortcuts Streamlit UI.")
    parser.add_argument("--host", default=None, help="Overrides server address (default 0.0.0.0)")
    parser.add_argument("--port", type=int, default=None, help="Overrides server port (default 8501)")
    args = parser.parse_args()

    # Fall back to .env WEB_HOST/WEB_PORT if not overridden (reuse Gradio defaults for consistency)
    host = args.host
    port = args.port
    if host is None or port is None:
        try:
            from app.config import WEB_HOST, WEB_PORT  # noqa: WPS433
            if host is None:
                host = WEB_HOST or "0.0.0.0"
            if port is None:
                # Streamlit default is 8501; keep Gradio's 7860 only for Gradio
                port = 8501 if WEB_PORT == 7860 else WEB_PORT
        except Exception:
            host = host or "0.0.0.0"
            port = port or 8501

    cmd = [
        sys.executable, "-m", "streamlit", "run", str(APP),
        "--server.address", str(host),
        "--server.port", str(port),
        "--server.headless", "true",
    ]
    print(f"Starting Streamlit: {' '.join(cmd)}")
    raise SystemExit(subprocess.call(cmd))


if __name__ == "__main__":
    raise SystemExit(main())
