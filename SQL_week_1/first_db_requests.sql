SELECT name, Year, ALIGN, FIRST_APPEARANCE, APPEARANCES
FROM MarvelCharacters
WHERE HAIR = 'Bald'
    AND ALIGN = 'Bad Characters'
    AND Year BETWEEN 1990 AND 1999
    AND Year IS NOT NULL
ORDER BY APPEARANCES DESC;

SELECT name, identify, FIRST_APPEARANCE, EYE
FROM MarvelCharacters
WHERE identify = 'Secret Identity'
    AND EYE NOT IN ('Blue Eyes', 'Brown Eyes', 'Green Eyes')
    AND FIRST_APPEARANCE IS NOT NULL
ORDER BY FIRST_APPEARANCE ASC;

SELECT name, HAIR
FROM MarvelCharacters
WHERE HAIR = 'Variable Hair';

SELECT name, SEX, EYE
FROM MarvelCharacters
WHERE SEX = 'Female Characters'
    AND EYE IN ('Gold Eyes', 'Amber Eyes');



