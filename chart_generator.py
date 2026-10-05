from PIL import Image, ImageDraw, ImageFont
import textwrap


def get_font(size, bold=False):
    try:
        if bold:
            return ImageFont.truetype(
                "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
                size
            )
        return ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            size
        )
    except:
        return ImageFont.load_default()


def generate_food_chart(condition, foods, care):

    width = 1000
    height = 900

    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    title_font = get_font(42, True)
    heading_font = get_font(30, True)
    body_font = get_font(24)

    # Title
    draw.text(
        (50, 40),
        "🥗 Supportive Recovery Guide",
        font=title_font,
        fill="black"
    )

    draw.text(
        (50, 105),
        f"Condition / Symptoms: {condition}",
        font=heading_font,
        fill="black"
    )

    # Food section
    draw.rounded_rectangle(
        (40, 170, 960, 500),
        radius=25,
        outline="black",
        width=3
    )

    draw.text(
        (70, 200),
        "🍎 Foods & Fluids That May Support Recovery",
        font=heading_font,
        fill="black"
    )

    y = 260

    for food in foods:

        wrapped = textwrap.wrap(food, width=55)

        draw.text(
            (80, y),
            "• " + wrapped[0],
            font=body_font,
            fill="black"
        )

        y += 40

        for line in wrapped[1:]:
            draw.text(
                (110, y),
                line,
                font=body_font,
                fill="black"
            )
            y += 35

        y += 10

    # Care section
    draw.rounded_rectangle(
        (40, 530, 960, 820),
        radius=25,
        outline="black",
        width=3
    )

    draw.text(
        (70, 560),
        "🛌 Self-Care & Recovery Tips",
        font=heading_font,
        fill="black"
    )

    y = 620

    for item in care:

        wrapped = textwrap.wrap(item, width=55)

        draw.text(
            (80, y),
            "• " + wrapped[0],
            font=body_font,
            fill="black"
        )

        y += 40

        for line in wrapped[1:]:
            draw.text(
                (110, y),
                line,
                font=body_font,
                fill="black"
            )
            y += 35

        y += 10

    return image
