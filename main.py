import itertools
import subprocess
import sys
import threading
import time
from pathlib import Path


class ImageBgRemoverApp:
    def __init__(self):
        self.name = "Image Background Remover"
        self.version = "1.0.0"
        self.author = "Eelco Greidanus"
        self.model = "birefnet-massive"
        self.spinner = self.Spinner()

    class Spinner:
        def __init__(self):
            self.running = False
            self.start_time = None

        def start(self):
            self.running = True
            self.start_time = time.time()
            threading.Thread(target=self.spin, daemon=True).start()

        def stop(self):
            self.running = False

        def spin(self):
            for c in itertools.cycle("⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"):
                if not self.running:
                    break
                elapsed = int(time.time() - self.start_time)
                print(f"\r{c} Processing... {elapsed}s", end="", flush=True)
                time.sleep(0.1)
            print("\r" + " " * 80 + "\r", end="", flush=True)

    def log(self, msg):
        print(f"[{self.name}] {msg}")

    def title(self):
        blue = "\033[94m"
        reset = "\033[0m"
        print(
            blue
            + f"""
██╗██████╗ ██████╗
██║██╔══██╗██╔══██╗
██║██████╔╝██████╔╝
██║██╔══██╗██╔══██╗
██║██████╔╝██║  ██║
╚═╝╚═════╝ ╚═╝  ╚═╝

{self.name} v{self.version}
Author: {self.author}
"""
            + reset
        )

    def open_file_dialog(self):
        self.log("Choose a file to process")
        result = subprocess.run(
            ["zenity", "--file-selection", "--title=Select Image"],
            capture_output=True,
            text=True,
        )
        return result.stdout.strip() if result.returncode == 0 else None

    def save_file_dialog(self, default_name):
        self.log("Choose output location")
        result = subprocess.run(
            [
                "zenity",
                "--file-selection",
                "--save",
                "--confirm-overwrite",
                "--filename",
                default_name,
                "--title=Save Output",
            ],
            capture_output=True,
            text=True,
        )
        return result.stdout.strip() if result.returncode == 0 else None

    def run(self):
        self.title()
        self.log("Starting application")

        input_file = self.open_file_dialog()
        if not input_file:
            self.log("Cancelled by user")
            return

        input_file = Path(input_file)

        output_file = self.save_file_dialog(f"{input_file.stem}_nobg.png")
        if not output_file:
            self.log("Cancelled by user")
            return

        self.log(f"Input: {input_file}")
        self.log(f"Output: {output_file}")

        try:
            self.spinner.start()

            subprocess.run(
                ["rembg", "i", str(input_file), str(output_file), "-m", self.model],
                check=True,
            )

            self.spinner.stop()

            self.log("Done ✔")
            self.log(f"Saved: {output_file}")

        except Exception as e:
            self.spinner.stop()
            self.log(f"Error: {e}")


if __name__ == "__main__":
    app = ImageBgRemoverApp()
    app.run()
