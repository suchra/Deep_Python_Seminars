import os
import random
import string
import logging
import argparse

# Инициализация системы логирования
logging.basicConfig(level=logging.INFO, filename='file_generator.log', filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')


def generate_random_filename(length_min=6, length_max=30):
    length = random.randint(length_min, length_max)
    letters = string.ascii_letters + string.digits
    filename = ''.join(random.choice(letters) for _ in range(length))
    return filename


def generate_random_bytes(min_bytes=256, max_bytes=4096):
    num_bytes = random.randint(min_bytes, max_bytes)
    byte_list = [random.randint(0, 255) for _ in range(num_bytes)]
    return bytes(byte_list)


def create_files_with_extension(extension, num_files=42, **kwargs):
    try:
        for _ in range(num_files):
            filename = generate_random_filename(length_min=kwargs.get('length_min', 6),
                                                length_max=kwargs.get('length_max', 30)) + f".{extension}"
            file_size = random.randint(kwargs.get('min_bytes', 256), kwargs.get('max_bytes', 4096))
            file_content = generate_random_bytes(min_bytes=kwargs.get('min_bytes', 256),
                                                 max_bytes=kwargs.get('max_bytes', 4096))

            with open(filename, 'wb') as file:
                file.write(file_content)
                logging.info(f"Created file: {filename}")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate random files with a specified extension.')
    parser.add_argument('--extension', required=True, help='File extension to create (e.g., txt)')
    parser.add_argument('--num_files', type=int, default=42, help='Number of files to create')
    parser.add_argument('--length_min', type=int, default=6, help='Minimum length of filenames')
    parser.add_argument('--length_max', type=int, default=30, help='Maximum length of filenames')
    parser.add_argument('--min_bytes', type=int, default=256, help='Minimum file size in bytes')
    parser.add_argument('--max_bytes', type=int, default=4096, help='Maximum file size in bytes')
    args = parser.parse_args()

    create_files_with_extension(
        extension=args.extension,
        num_files=args.num_files,
        length_min=args.length_min,
        length_max=args.length_max,
        min_bytes=args.min_bytes,
        max_bytes=args.max_bytes
    )