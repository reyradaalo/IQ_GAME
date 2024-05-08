import random


class EasyQuestion:
    def __init__(self):
        self.questions = [
            ("What is the capital city of France?", "paris"),
            ("Who wrote the famous play Romeo and Juliet?", "william shakespeare"),
            ("What is the chemical symbol for water?", "h20"),
            ("Which planet is known as the Red Planet?", "mars"),
            ("Who painted the Mona Lisa?", "leonardo da vinci"),
            ("What is the largest ocean on Earth?", "pacific ocean"),
            ("What is the tallest mountain in the world?", "mount everest"),
            ("Which country is known as the Land of the Rising Sun?", "japan"),
            ("What is the currency of Japan?", "japanese yen"),
            ("Who is the author of the Harry Potter book series?", "j.k. rowling"),
            ("What is the capital city of Australia?", "canberra"),
            ("Who wrote the novel To Kill a Mockingbird?", "Harper Lee"),
            ("What is the symbol for the chemical element gold?", "Au"),
            ("What is the largest mammal in the world?", "Blue whale"),
            ("What is the largest organ in the human body?", "Skin"),
            ("Who is known as the Father of Computers?", "Charles Babbage"),
            ("What is the currency of the United Kingdom?", "Pound sterling"),
            ("Who painted the ceiling of the Sistine Chapel?", "Michelangelo"),
            ("What is the capital city of Italy?", "Rome"),
            ("Who discovered penicillin?", "Alexander Fleming"),
            ("What is the largest continent by land area?", "Asia"),
            ("Who is the current President of the United States?", "Joe Biden"),
            ("What is the square root of 64?", "8"),
            ("Who is known as the Father of Geometry?", "Euclid"),
            ("What is the capital city of China?", "Beijing"),
            ("Who wrote the play Hamlet?", "William Shakespeare"),
            ("What is the chemical symbol for oxygen?", "O"),
            ("What is the largest desert in the world?", "Antarctic Desert"),
            ("What is the smallest country in the world?", "Vatican City"),
            ("Who composed the Moonlight Sonata?", "Ludwig van Beethoven"),
            ("What is the capital city of Russia?", "Moscow"),
            ("Who was the first person to walk on the moon?", "Neil Armstrong"),
            ("What is the largest planet in our solar system?", "Jupiter"),
            ("Who wrote the novel Pride and Prejudice?", "Jane Austen"),
            ("What is the chemical symbol for carbon?", "C"),
            ("Who is known as the Father of Modern Physics?", "Albert Einstein"),
            ("What is the largest city in the United States?", "New York City"),
            ("Who painted the Starry Night?", "Vincent van Gogh"),
            ("What is the currency of France?", "Euro"),
            ("Who is the Greek god of the sea?", "Poseidon"),
            ("What is the capital city of Spain?", "Madrid"),
            ("Who discovered electricity?", "Benjamin Franklin"),
            ("What is the chemical symbol for sodium?", "Na"),
            ("What is the longest river in the world?", "Nile"),
            ("Who wrote the novel 1984?", "George Orwell"),
            ("What is the capital city of Brazil?", "Brasilia"),
            ("Who is known as the Father of Medicine?", "Hippocrates"),
            ("What is the chemical symbol for iron?", "Fe"),
            ("What is the tallest animal in the world?", "Giraffe"),
            ("What is the chemical symbol for gold?", "Au")

        ]
        random.shuffle(self.questions)
        self.asked_indices = set()

    def get_question(self):
        remaining_indices = [i for i in range(len(self.questions)) if i not in self.asked_indices]
        if not remaining_indices:
            self.asked_indices.clear()
            remaining_indices = list(range(len(self.questions)))

        index = random.choice(remaining_indices)
        self.asked_indices.add(index)
        return self.questions[index]


class HardQuestion:
    def __init__(self):
        self.questions = [
            ("What is the opposite of ESPOUSE?", "oppose"),
            ("What color is CINNABAR?", "vermillion"),
            ("What is the opposite of SONOROUS?", "soft"),
            ("What is the meaning of SHRIKE?", "bird"),
            ("What is kept in a BINNACLE?", "compass"),
            ("What is the meaning of LIBRETTO?", "words of an opera"),
            ("SINGLE is to ONE as CIPHER is to?", "zero"),
            ("What is the meaning of PANACHE?", "swagger"),
            ("What would you be wearing if you wore GLEN-GARRY?", "a cap"),
        ]
        random.shuffle(self.questions)
        self.asked_indices = set()

    def get_question(self):
        remaining_indices = [i for i in range(len(self.questions)) if i not in self.asked_indices]
        if not remaining_indices:
            self.asked_indices.clear()
            remaining_indices = list(range(len(self.questions)))

        index = random.choice(remaining_indices)
        self.asked_indices.add(index)
        return self.questions[index]


class MediumQuestion:
    def __init__(self):
        self.questions = [
            ("Nearest galaxy to the Milky Way?", "andromeda"),
            ("First woman in space?", "valentina tereshkova"),
            ("Average Earth-Moon distance?", "384,400 kilometers"),
            ("Largest moon in solar system?", "ganymede"),
            ("Discoverer of Jupiter's largest moons?", "galileo galilei"),
            ("Moon-landing spacecraft name?", "apollo 11"),
            ("First American astronaut's orbiting craft?", "friendship 7"),
            ("Name of first artificial satellite?", "sputnik 1"),
            ("Cause of Northern and Southern Lights?", "solar wind interacting with earth's magnetic field"),
            ("Planet with most moons?", "jupiter"),
            ("Main component of the Sun?", "hydrogen"),
            ("Force keeping planets in orbit?", "gravity"),
            ("First spacecraft to Pluto?", "new horizons"),
            ("Largest volcano in the solar system?", "olympus mons"),
            ("First human to spacewalk?", "alexei leonov"),
            ("First living organisms in space?", "fruit flies"),
            ("First orbiting space station name?", "skylab"),
            ("Farthest visited solar system object?", "voyager 1"),
            ("Titan-landing spacecraft?", "huygens"),
            ("First space telescope name?", "hubble space telescope"),
            ("First Mercury-orbiting craft?", "mariner 10"),
            ("Planet with distinctive rings?", "saturn"),
            ("Theory explaining the universe's origin?", "big bang theory"),
            ("First American woman in space?", "sally ride"),
            ("Comet-landing spacecraft name?", "philae"),
            ("First human Moon mission name?", "apollo 11"),
            ("Mars water evidence mission?", "mars science laboratory "),
            ("Mars-Jupiter asteroid belt name?", "asteroid belt"),
            ("Jupiter moons discoverer?", "galileo galilei"),
            ("Great Red Spot discoverer spacecraft?", "voyager 1"),
            ("Venus atmosphere studying craft?", "venus express"),
            ("Longest day planet name?", "venus"),
            ("First Mercury-visited craft?", "mariner 10"),
            ("Heliocentric model proposer?", "nicolaus copernicus"),
            ("Star movement due to Earth's rotation?", "apparent motion"),
            ("First asteroid orbiting spacecraft?", "near shoemaker"),
            ("Pluto close-up image spacecraft?", "new horizons"),
            ("Saturn rings studying spacecraft?", "cassini"),
            ("Mars past water evidence mission?", "mars science laboratory"),
            ("Southern hemisphere stars mapper?", "hipparcos"),
            ("Neptune's Great Dark Spot observing craft?", "voyager 2"),
            ("Solar system's highest mountain planet?", "olympus mons "),
            ("Massive star collapse into black hole phenomenon?", "supernova"),
            ("Titan atmosphere studying craft?", "huygens"),
            ("Dwarf planet Ceres studying spacecraft?", "dawn"),
            ("Planetary motion laws proposer?", "johannes kepler"),
            ("Mars organic molecules discovery mission?", "mars science laboratory"),
            ("Venus soft landing spacecraft?", "venera 7"),
            ("Expanding universe theory name?", "big bang theory"),
            ("Closest star to Earth?", "proxima centauri"),

        ]
        random.shuffle(self.questions)
        self.asked_indices = set()

    def get_question(self):
        remaining_indices = [i for i in range(len(self.questions)) if i not in self.asked_indices]
        if not remaining_indices:
            self.asked_indices.clear()
            remaining_indices = list(range(len(self.questions)))

        index = random.choice(remaining_indices)
        self.asked_indices.add(index)
        return self.questions[index]
