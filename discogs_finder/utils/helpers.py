def filter_list(
    d, releases_ids, want_treshold, have_treshold, user_style, include_styles, file_path
):

    # Normalize user style
    user_style = user_style if isinstance(user_style, list) else [user_style]
    user_style = [s.lower() for s in user_style]

    # Iterate in releases and print only filtered ones
    for id in releases_ids:
        try:
            release = d.release(id)

            # Normalise release style
            release_style = release.styles
            release_style = (
                release_style if isinstance(release_style, list) else [release_style]
            )
            release_style = [r.lower() for r in release_style]

            # Apply want have filter
            if (
                release.community.want > want_treshold
                or release.community.have > have_treshold
            ):
                continue

            # Set style match
            if include_styles == "no":
                style_match = set(user_style) == (release_style)

            else:
                style_match = set(user_style).issubset(set(release_style))

            if style_match:
                print(release.url)
                # call function
                write_on_file(release.url, file_path)

        except Exception as e:
            print(f"Error fetching: {e}")

    print("Done!")


def write_on_file(url, file_path):
    with open(file_path, "a") as f:
        f.write(f'<a href="{url}" target="_blank">{url}</a><br>\n')
