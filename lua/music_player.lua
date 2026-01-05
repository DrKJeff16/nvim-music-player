local M = {}

M.browse = function()
	local telescope = require("telescope.builtin")

	telescope.find_files({
		prompt_title = "🎵 Music Library",
		cwd = vim.fn.expand("~/Music"),
		find_command = { "fdfind", "--type", "f", "--extension", "mp3", "--extension", "flac" },
		attach_mappings = function(promp_bufnr, map)
			local actions = require("telescope.actions")
			local actions_state = require("telescope.actions.state")

			map("i", "<CR>", function()
				local selection = actions_state.get_selected_entry()
				actions.close(promp_bufnr)

				if selection and selection.path then
					vim.cmd("MusicPlay " .. vim.fn.fnameescape(selection.path))
				end
			end)

			return true
		end,
	})
end

return M

