# ===============================
# nicolas.leblanc3@mail.mcgill.ca
# ===============================

import random
import spreadsheetTool

def trialGen(lInput=None, iNmbPoliticians=248, iPercentageGrey=25, iNmbComparison=33, iMaxReoccurence=8):
    '''
    Introduction: This is the main function. Note that it generates its own random rating in
    order to ease the development of further code. The goal of this function is
    to present the test subject with a randomly generated set of trials.
    '''
    # First, we generate ratings for the politicians. In a real life scenario, these
    # ratings would be acquired by asking the test subject to rate a series of 
    # politician pictures from -3 to 3.
    if lInput:
        lRatings = []
        for i in range(len(lInput)):
            sRating = i
            lRatings.append(assignParty(lInput[i], iPercentageGrey, sRating))
    else:
        lRatings = generateRatingsAndParty(iNmbPoliticians, iPercentageGrey)
        
    # We will keep track of the number of times a politician is presented
    # to the test subject
    for x in range(len(lRatings)):
        for y in range(len(lRatings[x])):
            lRatings[x][y] += "_count0"
    
    # We then run the "generateComparisonList" function several times in order to generate
    # random comparisons of politicians with various rating differences and frame
    # colours to be presented to the test subject.
    lComparissonList10 = generateComparisonList(lRatings, iNmbComparison, 0, "grey", "grey", iMaxReoccurence)
    lComparissonList11 = generateComparisonList(lRatings, iNmbComparison, 1, "grey", "grey", iMaxReoccurence)
    lComparissonList12 = generateComparisonList(lRatings, iNmbComparison, 2, "grey", "grey", iMaxReoccurence)
    lComparissonList02 = generateComparisonList(lRatings, iNmbComparison, 2, "grey", "red", iMaxReoccurence)
    lComparissonList00 = generateComparisonList(lRatings, iNmbComparison, 0, "grey", "red", iMaxReoccurence)
    lComparissonList01 = generateComparisonList(lRatings, iNmbComparison, 1, "grey", "red", iMaxReoccurence)
    
    # We print the content of the comparison lists to the screen
    print "\n============================\n"
    print "\nlist of comparison with difference =0 and different colours is:\n"
    for i in range(len(lComparissonList00)):
        print lComparissonList00[i]
    print "\n---------------------------\n"
    print "\nlist of comparison with difference =1 and different colours is:\n"
    for i in range(len(lComparissonList01)):
        print lComparissonList01[i]
    print "\n---------------------------\n"
    print "\nlist of comparison with difference =2 and different colours is:\n"
    for i in range(len(lComparissonList02)):
        print lComparissonList02[i]
    print "\n---------------------------\n"
    print "\nlist of comparison with difference =0 and same colours is:\n"
    for i in range(len(lComparissonList10)):
        print lComparissonList10[i]
    print "\n---------------------------\n"
    print "\nlist of comparison with difference =1 and same colours is:\n"
    for i in range(len(lComparissonList11)):
        print lComparissonList11[i]
    print "\n---------------------------\n"
    print "\nlist of comparison with difference =2 and same colours is:\n"
    for i in range(len(lComparissonList12)):
        print lComparissonList12[i]
    print "\n============================\n"
    
    
def generateComparisonList(lRatings, iNmbComparison, iDifference, sParty0, sParty1, iMaxReoccurence=8):
    '''
    Introduction: This function is used to generate the comparison list. It avoids duplicate comparisons and
    ensures the same politician is not used more than the maximum amount of reoccurence it is allowed.
    
    Input Param: lRatings
    Type: List
    Def: A list of list containing the population of politicians from which 
         the comparisons are generated. 1st element of this list is a list of politicians with
         rating of 0. 2nd element of this list is a list of politicians with rating of 1. 3rd
         element of this list is a list of politicians with rating of 2. 4th element of this
         list is a list of politicians with rating of 3.
    
    Input Param: iNmbComparison
    Type: Int
    Def: The number of comparisons we wish to generate.
    
    Input Param: iDifference
    Type: Int
    Def: The difference between politicians compared.
    
    Input Param: sParty0
    Type: String
    Def: The colour of the 1st frame of the two frames of our comparisons.
    
    Input Param: sParty1
    Type: String
    Def: The colour of the 2nd frame of the two frames of our comparisons.
    
    Input Param: iMaxReoccurence
    Type: Int
    Def: The maximal number of times a politician can be used in the whole test.
    
    Output Param: lComparissonList
    Type: List
    Def: A list containing lists of unique comparison generated.
    '''
    lComparissonList = []
    # We iterate through this random generation process until we have desired number of comparisons
    while(len(lComparissonList)<iNmbComparison):
        # We randomly select the first politicians of every comparisons we wish to generate.
        # Note that the rating of these politicians are random as they were randomly assigned in a previous step.
        x = random.choice(range(len(lRatings)))
        y = random.choice(range(len(lRatings[x])))
        # We check if politician was not used more than allowed number of times
        # and if politician is of the desired party/colour.
        if (("count%s"%(iMaxReoccurence)) not in lRatings[x][y] and
            sParty0 in lRatings[x][y]):
            # If politician meets the above criteria, count of first politician is incremented to ensure
            # politician does not get used more than allowed number of times. We also
            # create one element of the comparison list.
            lRatings[x][y] = lRatings[x][y].replace(("count"+lRatings[x][y].split("count")[-1]),
                                                    "count"+str((int(lRatings[x][y].split("count")[-1])+1)))
            lComparissonList.append([lRatings[x][y]])
    
    # Now that lComparissonList is of the right length, we must complete its elements by assigning a
    # second politician to them.
    for i in range(len(lComparissonList)):
        lComparisson = lComparissonList[i]
        # We iterate through this random generation process until we find the second politician
        # for our given comparison.
        while(len(lComparisson)<2):
            # We randomly select the second politicians.
            x = random.choice(range(len(lRatings)))
            y = random.choice(range(len(lRatings[x])))
            # We verify that the rating difference is as required, and that the
            # count are not greater than the maximum value allowed.
            if ((("count%s"%iMaxReoccurence) not in lRatings[x][y]) and
                ((lComparisson[0].split("_")[0]) not in lRatings[x][y]) and
                (abs(int(lComparisson[0].split("_")[1]) -int(lRatings[x][y].split("_")[1])) == iDifference) and
                (sParty1 in lRatings[x][y])):
                # Here, we use a boolean "bDuplicate" to keep track of duplicate comparisons.
                # IE, if comparison already exists, "bDuplicate" will be set to true and
                # comparison will be discarded.
                bDuplicate = False
                # We verify if comparison between the two politicians already exists.
                for j in range(len(lComparissonList)):
                    if len(lComparissonList[j]) == 2:
                        if (lComparisson[0].split("_")[0] in lComparissonList[j][0] and
                            lRatings[x][y].split("_")[0] in lComparissonList[j][1] or
                            lComparisson[0].split("_")[0] in lComparissonList[j][1] and
                            lRatings[x][y].split("_")[0] in lComparissonList[j][0]):
                            # if comparison between the two politicians already exists,
                            # we set "bDuplicate" to true such that comparison will be discarded.
                            bDuplicate = True
                # If comparison is genuine (not duplicated), comparison must be valid. Thus, we update our
                # comparison list with the new comparison and increment the count of the second politician.
                if bDuplicate == False:
                    lRatings[x][y] = lRatings[x][y].replace(("count"+lRatings[x][y].split("count")[-1]),
                                                            "count"+str((int(lRatings[x][y].split("count")[-1])+1)))
                    lComparissonList[i].append(lRatings[x][y])
    return lComparissonList
    
    
def generateRatingsAndParty(iNmbPoliticians=248/2, iPercentageGrey=25):
    '''
    Introduction: This function is used to generate the random ratings of the politicians. In 
    a real life scenario, this function is not needed as the ratings would be provided
    by the test subject in the first part of the experiment. However, this function is still usefull to further
    develop this program as it provides the programmer with a tool to test his code.
    
    Input Param: iNmbPoliticians
    Type: Int
    Def: The number of politicians to be rated. Note that only non-negative ratings are relevant for this test. Hence,
         in a real life scenario, you might show the test subject 248 politicians and only retain half for the
         comparisson, but since this is a program, we right away only generate the ratings out of 248/2 politician
         and assign them ratings between 0 and 3.
    
    Input Param: iPercentageGrey
    Type: Int
    Def: The percentage of politicians with a grey frame. Implicitely, the percentage of
         politician with a red frame will be the difference out of 100%.
    
    Output Param: lRatings
    Type: List
    Def: A list containing lists of politicians with the same ratings, namely: 0, 1, 2 & 3.
    '''
    iNmbPoliticians
    lPoliticians = []
    # We populate our list "lPoliticians" with the right number of politicians.
    # Politicians are represented as alphanumeric strings.
    for i in range(iNmbPoliticians):
        lPoliticians.append("politician%s"%i)
    
    # We sample 1/4 of the politicians and store them in a list. All politicians stored 
    # in thassignParty(lSampleRated, iPercentageGrey, sRating)is list are now assumed to have rating = 0. We also remove these politicians
    # from "lPoliticians" to ensure they only have a single rating value assigned to them.
    # Politician's party/colours are also assigned at this step of the process to ensure
    # a given politician is only assigned to a single party throughout subsequent processes.
    lSampleRated0 = random.sample(lPoliticians,iNmbPoliticians/4)
    removeFromList(lSampleRated0, lPoliticians)
    assignParty(lSampleRated0, iPercentageGrey, 0)
    
    # We do the same this, but for politicians with rating =1.
    lSampleRated1 = random.sample(lPoliticians,iNmbPoliticians/4)
    removeFromList(lSampleRated1, lPoliticians)
    assignParty(lSampleRated1, iPercentageGrey, 1)
    
    # We do the same this, but for politicians with rating =2.
    lSampleRated2 = random.sample(lPoliticians,iNmbPoliticians/4)
    removeFromList(lSampleRated2, lPoliticians)
    assignParty(lSampleRated2, iPercentageGrey, 2)
    
    # We do the same this, but for politicians with rating =3.
    lSampleRated3 = random.sample(lPoliticians,iNmbPoliticians/4)
    removeFromList(lSampleRated3, lPoliticians)
    assignParty(lSampleRated3, iPercentageGrey, 3)
    
    # We return a list containing lists of politicians with the same ratings, namely: 0, 1, 2 & 3.
    lRatings = [lSampleRated0,lSampleRated1,lSampleRated2,lSampleRated3]
    return lRatings


def assignParty(lSampleRated, iPercentageGrey, sRating):
    '''
    Introduction: This function is used to assign a party to politicians in a list with the same rating.
    
    Input Param: lSampleRated
    Type: List
    Def: A list containing string representation of politicians with the same ratings.
    
    Input Param: iPercentageGrey
    Type: Int
    Def: The percentage of politicians with a grey frame. Implicitely, the percentage of
         politician with a red frame will be the difference out of 100%.
    
    Input Param: sRating
    Type: String
    Def: The rating of the politicians in this group to be appended to the string representation of the politicians.
    '''
    lParty = []
    # Number of grey and red are computed from iPercentageGrey
    iNmbGrey = int(float(iPercentageGrey)/100*len(lSampleRated))
    iNmbred = len(lSampleRated) - iNmbGrey
    # We then populate the "lParty" list accordingly such that it
    # contains the right amount of desired "iPercentageGrey" and that
    # it has same number of elements as "lSampleRated"
    for i in range(iNmbGrey):
        lParty.append("grey")
    for i in range(iNmbred):
        lParty.append("red")
    # We then assign a colour(party) to each politician in lSampleRated.
    # This is done by String appendation. We also append the rating for later use.
    for i in range(len(lSampleRated)):
        sParty = random.choice(lParty)
        removeFromList([sParty], lParty)
        lSampleRated[i] = lSampleRated[i].split("_")[0] + ("_%s_%s"%(sRating, sParty))
        
    return lSampleRated
    

def removeFromList(lList1, lList2):
    '''
    Introduction: This function is used to remove a list of individual elements from within another list.
    
    Input Param: lList1
    Type: List
    Def: lList1 indicates which elements must be removed in lList2.
    
    Input Param: lList2
    Type: List
    Def: lList2 is a list from which elements will be removed.
    '''
    for element in lList1:
        lList2.remove(element)


# This calls the main function of this file, mainly: "trialGen"
trialGen()
a = spreadsheetTool.getOrderedInput()
trialGen(a, iNmbComparison=33)

