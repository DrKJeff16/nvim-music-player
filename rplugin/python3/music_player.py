"""Python code for ``nvim-music-player``."""
from os.path import exists, realpath
from shutil import which
from subprocess import DEVNULL, Popen
from typing import NoReturn, Tuple

import pynvim


@pynvim.plugin
class MusicPlayer:
    """
    Music player Neovim plugin class.

    Parameters
    ----------
    nvim : pynvim.Nvim
        The Neovim instance.
    """

    nvim: pynvim.Nvim
    process: Popen | None

    def __init__(self, nvim: pynvim.Nvim):
        self.nvim: pynvim.Nvim = nvim
        self.process: Popen | None = None
        self.nvim.out_write("🎵 nvim-music-player loaded\n")

    @pynvim.command("MusicPlay", nargs=1, complete="file")
    def play(self, args: Tuple[str]) -> NoReturn:
        """Start playing the given music file."""
        if not which("mpv"):
            self.nvim.err_write("Unable to find mpv in PATH\n")
            return

        path: str = realpath(args[0].replace('\\ ', ' '))
        if not exists(path):
            self.nvim.err_write(f"❌ File not found: {path}\n")
            return

        if self.process is not None:
            self.process.terminate()

        self.process = Popen(["mpv", "--no-video", path], stdout=DEVNULL, stderr=DEVNULL)
        self.nvim.out_write(f"🎶 Playing: {path}\n")

    @pynvim.command("MusicStop", nargs=0)
    def stop(self) -> NoReturn:
        """Stop the music player."""
        if self.process is not None:
            self.process.terminate()
            self.process = None
            self.nvim.out_write("⏹ Music stopped\n")
            return

        self.nvim.out_write("Music already stopped\n")

# vim: set ts=4 sts=4 sw=4 et ai si sta:
