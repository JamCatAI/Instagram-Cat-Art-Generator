from generate_art import generate_art
from post_to_instagram import post_image

if __name__ == "__main__":
    input_image = "input_images/cat1.jpg"
    prompt = "A magical Pixar-style painting of a cute cat with glowing eyes and galaxy background"
    generated_image = generate_art(input_image, prompt)

    caption = "✨🐾 Our AI worked magic again! #CatArt #JamCatAI #Meowgical"
    post_image(generated_image, caption)
