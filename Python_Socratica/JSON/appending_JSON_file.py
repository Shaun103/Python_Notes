import json

def main() -> None:
    path = '/Users/User/Desktop/Python/Python_Socratica/JSON/movie_1.txt'

    with open(path, 'r+') as file:
        data = json.load(file) # loading the file
        # grabing column and appending list
        data['actors'] = ["Ethan Hawke", "Uma Thurman", "Alan Arkin", "John Doe", "Loren Dean"]
        # reset file position to beginning
        file.seek(0)
        # writing to file
        json.dump(data, file, indent=2)
        # removes remaining part
        file.truncate()

    print('..transfer complete')
if __name__ == "__main__":
    main() 