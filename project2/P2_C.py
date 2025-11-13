import console_gfx

def open_menu():
    print("RLE Menu")
    print("--------")
    print("0. Exit")
    print("1. Load File")
    print("2. Load Test Image")
    print("3. Read RLE String")
    print("4. Read RLE Hex String")
    print("5. Read Data Hex String")
    print("6. Display Image")
    print("7. Display RLE String")
    print("8. Display Hex RLE Data")
    print("9. Display Hex Flat Data")
    print()
    return int(input("Select a Menu Option: "))

def main():
    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    console_gfx.display_image(console_gfx.test_rainbow)
    print()

    image_data = None

    while True:
        print()
        option = open_menu()

        if option == 0:
            break

        elif option == 1:
            file_name = input("Enter name of file to load: ")
            image_data = console_gfx.load_file(file_name)

        elif option == 2:
            image_data = console_gfx.test_image
            print("Test image data loaded.")

        elif option == 3:
            rle_string = input("Enter an RLE string to be decoded: ")
            rle_data = string_to_rle(rle_string)
            image_data = decode_rle(rle_data)
        
        elif option == 4:
            rle_hex_string = input("Enter the hex string holding RLE data: ")
            image_data = decode_rle(string_to_data(rle_hex_string))


        elif option == 5:
            data_hex_string = input("Enter the hex string holding flat data: ")
            image_data = string_to_data(data_hex_string)


        elif option == 6:
            if image_data is not None:
                print("Displaying image...")
                console_gfx.display_image(image_data)
            else:
                print("(no data)")

        elif option == 7:
            if image_data is not None:
                rle_data = encode_rle(image_data)
                print("RLE representation:", to_rle_string(rle_data))
            else:
                print("(no data)")

        elif option == 8:
            if image_data is not None:
                rle_data = encode_rle(image_data)
                print("RLE hex values:", to_hex_string(rle_data))
            else:
                print("(no data)")

        elif option == 9:
            if image_data is not None:
                print("Flat hex values:", to_hex_string(image_data))
            else:
                print("(no data)")





def to_hex_string(data):
    return ''.join(format(n,'x') for n in data)

def count_runs(flat_data): 
    if not flat_data:
        return 0
    runs = 1
    current = flat_data[0]
    count = 1
    for value in flat_data[1:]:
        if value == current and count < 15:
            count += 1
        else:
            runs += 1
            current = value
            count = 1
    return runs

def encode_rle(flat_data):
    if not flat_data:
        return []
    rle = []
    current = flat_data[0]
    count = 1
    for value in flat_data[1:]:
        if value == current and count < 15:
            count += 1
        else:
            rle.extend([count, current])
            current = value
            count = 1
    rle.extend([count, current])
    return rle

def get_decoded_length(rle_data):
    return sum(rle_data[i] for i in range(0, len(rle_data), 2))

def decode_rle(rle_data):
    flat_data = []
    for i in range(0, len(rle_data), 2):
        length = rle_data[i]
        value = rle_data[i + 1]
        flat_data.extend([value] * length)
    return flat_data

def string_to_data(data_string):
    return [int(c, 16) for c in data_string]

def to_rle_string(rle_data):
    parts = []
    for i in range(0, len(rle_data), 2):
        count = rle_data[i]
        value = rle_data[i + 1]
        parts.append(f"{count}{format(value, 'x')}")
    return ':'.join(parts)


def string_to_rle(rle_string):
    rle_data = []
    runs = rle_string.split(':')
    for run in runs:
        count = int(run[:-1])
        value = int(run[-1], 16)
        rle_data.extend([count, value])
    return rle_data

if __name__ == "__main__":
    main()