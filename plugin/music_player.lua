vim.api.nvim_create_user_command("MusicBrowse", function()
	require("music_player").browse()
end, {})
