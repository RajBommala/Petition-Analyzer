import unittest
import csv
from main import PetitionAnalyzer

class TestPetitionAnalyzer(unittest.TestCase):
    
    def test_analyze_petitions(self):
        analyzer = PetitionAnalyzer('test_petitions.json', 'test_petitions.csv')
        analyzer.run()
        
        with open('test_petitions.csv', 'r') as f:
            rows = [row for row in csv.reader(f)]
            self.assertEqual(rows[0], ['petition_id', 'should', 'their', 'people', 'government', 'there', 'would', 'which', 'being', 'children', 'these', 'public', 'other', 'years', 'british', 'after', 'health', 'those', 'currently', 'could', 'every'])
            self.assertEqual(rows[1], ['1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0'])
            self.assertEqual(rows[2], ['2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])

if __name__ == '__main__':
    unittest.main()