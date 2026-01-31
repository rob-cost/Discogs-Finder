def filter_list(d, releases_ids, want_treshold, style):

    style = style if isinstance(style, list) else [style]
    style = [s.lower() for s in style]

    for id in releases_ids:
        try:
            release = d.release(id)
            release_style = release.styles
            release_style = (
                release_style if isinstance(release_style, list) else [release_style]
            )
            release_style = [r.lower() for r in release_style]

            if release.community.want <= want_treshold and set(style) == set(
                release_style
            ):
                print(release.url)

        except Exception as e:
            print(f"Error fetching: {e}")
