vim.api.nvim_create_user_command("MusicBrowse", function()
	require("music_player").browse()
end, {})
-- vim: set ts=4 sts=4 sw=0 noet ai si sta:
