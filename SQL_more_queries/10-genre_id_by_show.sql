-- List all shows contained in `hbtn_0d_tvshows` that have at least one genre linked.
SELECT tv_show_genres.genre_id, tv_shows.title FROM tv_shows
JOIN  tv_shows_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_show_genres.genre_id, tv_shows.title;
