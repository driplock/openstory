StoryParser - Parser formatted text and transforms it to ordered dictionary structure.

Example:

'1': { 'Narrator': 'What the narrator is saying' },
     { 'Character': 'What the character is sayung' }


PageObjectHandler - Page object handler takes in StoryParser output and store it 
so other objects does need to understand the structure of what StoryParser spits out.

Notes:
- This decouples story parser object to any other object whi will need story parser
- But this also means it will have dependency on StoryParser object structure.

HTMLPageWriter - This will write the HTML structure that takes an input from PageObjectHandler

Note: Should there be another object to write it as AngularJS format?
