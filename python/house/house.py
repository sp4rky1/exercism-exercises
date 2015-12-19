things = ["the house that Jack built.",
          "the malt\n",
          "the rat\n",
          "the cat\n",
          "the dog\n",
          "the cow with the crumpled horn\n",
          "the maiden all forlorn\n",
          "the man all tattered and torn\n",
          "the priest all shaven and shorn\n",
          "the rooster that crowed in the morn\n",
          "the farmer sowing his corn\n",
          "the horse and the hound and the horn\n"]

verbs = ["lay in ",
         "ate ",
         "killed ",
         "worried ",
         "tossed ",
         "milked ",
         "kissed ",
         "married ",
         "woke ",
         "kept ",
         "belonged to "]

def verse(number):
    result = "This is "
    for i in range(number)[::-1]:
        result += things[i+1] + "that " + verbs[i]
    return result + things[0]

def rhyme():
    return "\n\n".join([verse(i) for i in range(12)])