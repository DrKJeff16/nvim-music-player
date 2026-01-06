import pynvim
import subprocess
import os


@pynvim.plugin
class MusicPlayer:
    def __init__(self, nvim):
        self.nvim = nvim
        self.process = None
        self.nvim.out_write("🎵 nvim-music-player loaded\n")

    @pynvim.command("MusicPlay", nargs=1)
    def play(self, args):
        path_from_lua = args[0]
        actual_path = path_from_lua.replace('\\ ', ' ')
        path = os.path.expanduser(actual_path)

        if not os.path.exists(path):
            self.nvim.err_write(f"❌ File not found: {path}\n")
            return

        if self.process:
            self.process.terminate()

        self.process = subprocess.Popen(
            ["mpv", "--no-video", path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        self.nvim.out_write(f"🎶 Playing: {path}\n")

    @pynvim.command("MusicStop", nargs=0)
    def stop(self):
        if self.process:
            self.process.terminate()
            self.process = None
            self.nvim.out_write("⏹ Music stopped\n")

# vim: set ts=4 sts=4 sw=4 et ai si sta:
