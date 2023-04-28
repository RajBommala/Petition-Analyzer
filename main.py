import json
import csv
from collections import Counter

class PetitionAnalyzer:
    """The PetitionAnalyzer class to transform input JSON data into a new 
       CSV output file with one row per petition, ccontaing 21 columns
    """
    
    def __init__(self, input_file, output_file):
        """method for initializing analyzer object
        
        Args:
            input_file(JSON)
            output_file(CSV)
            
        Attributes:
            input_file(JSON): input JSON file
            output_file(CSV): output CSV file 
            petitions: empty list
            most_common_words: empty list 
        """
        self.input_file = input_file
        self.output_file = output_file
        self.petitions = []
        self.most_common_words = []
    
    def load_petitions(self):
        """The load_petitions() method reads the input JSON file and
           stores it as an attribute of the PetitionAnalyzer object (self.petitions).
           
           Returns: None
        """
        with open(self.input_file, 'r') as input:
            self.petitions = json.load(input)
    
    def get_most_common_words(self):
        """method to get 20 most common words of length 5 or more across all petitions.
        
           Returns: list 
        """
        #create word_count object to count the occurences of each word
        word_counts = Counter()
        
        #iterates over each petition in the list of petitions stored in the self.petitions attribute
        for petition in self.petitions:
            abstract = petition['abstract']['_value']
            word_counts.update(word.lower() for word in abstract.split() if len(word) >= 5)
        
        #retrieves the 20 most common words (by frequency) from the Counter object
        self.most_common_words = [word for word, count in word_counts.most_common(20)]
    
    def analyze_petitions(self):
        """analyze_petitions() takes the most common words across all petitions and 
        creates a CSV file with one row per petition, containing the petition ID and the count of 
        each of the most common words in that petition's abstract value
        
        Returns: None
        """
        
        #opens the output file in write mode and creates a csv.writer object to write data to the file.
        with open(self.output_file, 'w', newline='') as output:
            writer = csv.writer(output)
            
            # Write the header row with the column names
            header_row = ['petition_id'] + self.most_common_words
            writer.writerow(header_row)
            
            # Write the data rows with the petition IDs and word counts
            for i, petition in enumerate(self.petitions):
                abstract = petition['abstract']['_value']
                word_counts = Counter(word.lower() for word in abstract.split() if len(word) >= 5)
                row = [i+1] + [word_counts[word] for word in self.most_common_words]
                writer.writerow(row)
    
    def run(self):
        self.load_petitions()
        self.get_most_common_words()
        self.analyze_petitions()

if __name__ == '__main__':
    analyzer = PetitionAnalyzer('petitions.json', 'petitions.csv')
    analyzer.run()