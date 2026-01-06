---@class MusicPlayer
local M = {}

function M.browse()
	local fd_exe = ""
	if vim.fn.executable("fd") == 1 then
		fd_exe = "fd"
	elseif vim.fn.executable("fdfind") == 1 then
		fd_exe = "fdfind"
	else
		vim.notify("`fd` is not installed!", vim.log.levels.ERROR)
		return
	end

	require("telescope.builtin").find_files({
		prompt_title = "🎵 Music Library",
		cwd = vim.fn.expand("~/Music"),
		find_command = { fd_exe, "--type", "f", "--extension", "mp3", "--extension", "flac" },
		attach_mappings = function(promp_bufnr, map)
			map("i", "<CR>", function()
				local selection = require("telescope.actions.state").get_selected_entry()
				require("telescope.actions").close(promp_bufnr)
				if selection and selection.path then
					vim.cmd.MusicPlay(vim.fn.fnameescape(selection.path))
				end
			end)

			return true
		end,
	})
end

return M
-- vim: set ts=4 sts=4 sw=0 noet ai si sta:
