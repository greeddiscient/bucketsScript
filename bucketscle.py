import csv

class player(object):
    def __init__(self,firstName,lastName, teamName,teamAbbrev,playerNo,colorways):
        self.firstName=firstName
        self.lastName=lastName
        self.teamName=teamName
        self.teamAbbrev=teamAbbrev
        self.playerNo=playerNo
        self.colorways=colorways

sc30=player("Kyrie", "Irving", "Cleveland Cavaliers", "cle", 2,["White Home","Red Wine","Alternate Gold","Christmas '16"])
kt11=player("LeBron", "James", "Cleveland Cavaliers", "cle", 23,["White Home","Red Wine","Alternate Gold","Christmas '16"])
dg23=player("Kevin", "Love", "Cleveland Cavaliers", "cle", 0,["White Home","Red Wine","Alternate Gold","Christmas '16"])
kd35=player("JR", "Smith", "Cleveland Cavaliers", "cle", 5,["White Home","Red Wine","Alternate Gold","Christmas '16"])
# ai09=player("Tristan", "Thompson", "Cleveland Cavaliers", "cle", 13,["White Home","Red Wine","Alternate Gold","Christmas '16"])

totalImages=[
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8582.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8585.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8584.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8586.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8583.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8587.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8591.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8588.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8592.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8589.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223181717_IMG_8714.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223181634_IMG_8712.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223181739_IMG_8717.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223181641_IMG_8713.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223181730_IMG_8716.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223182253_IMG_8730.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223182221_IMG_8728.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223182256_IMG_8731.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223182227_IMG_8729.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223182300_IMG_8732.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315155034_IMG_8826.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315155115_IMG_8830.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315155043_IMG_8827.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315155119_IMG_8831.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315155048_IMG_8828.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315155601_IMG_8840.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315155841_IMG_8855.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315155646_IMG_8846.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315155752_IMG_8850.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315155632_IMG_8844.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315171405_IMG_8984.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315171844_IMG_8991.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315171824_IMG_8989.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315171851_IMG_8992.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315171424_IMG_8988.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315172019_IMG_8996.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315172109_IMG_9001.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315172043_IMG_9000.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315172113_IMG_9002.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315172027_IMG_8998.JPG?10139439430536178035",

"https://cdn.shopify.com/s/files/1/2019/6095/files/Smith_White_Front.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Smith_White_Back.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Smith_Gold_Front.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Smith_Gold_Back.JPG?13313192378586356337",

"https://cdn.shopify.com/s/files/1/2019/6095/files/Love_Gold_Front.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Love_Gold_Back.JPG?13313192378586356337",
]

imgsKI={
    "White Home":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8587.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8591.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8588.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8592.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8589.JPG10139439430536178035"
    ],
    "Red Wine":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/20170315155034_IMG_8826.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315155115_IMG_8830.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315155043_IMG_8827.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315155119_IMG_8831.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315155048_IMG_8828.JPG?10139439430536178035"
    ],
    "Christmas '16":[

    ],
    "Alternate Gold":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/20170315172019_IMG_8996.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315172109_IMG_9001.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315172043_IMG_9000.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315172113_IMG_9002.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315172027_IMG_8998.JPG?10139439430536178035"
    ]
}

imgsKL={
    "White Home":[

    ],
    "Red Wine":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/20170223182253_IMG_8730.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223182221_IMG_8728.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223182256_IMG_8731.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223182227_IMG_8729.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223182300_IMG_8732.JPG?10139439430536178035"
    ],
    "Christmas '16":[

    ],
    "Alternate Gold":[
    "https://cdn.shopify.com/s/files/1/2019/6095/files/Love_Gold_Front.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Love_Gold_Back.JPG?13313192378586356337",
    ]
}
imgsLBJ={
    "White Home":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8582.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8585.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8584.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8586.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8583.JPG?10139439430536178035"
    ],
    "Red Wine":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/20170315155601_IMG_8840.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315155841_IMG_8855.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315155646_IMG_8846.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315155752_IMG_8850.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315155632_IMG_8844.JPG?10139439430536178035"
    ],
    "Christmas '16":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/20170223181717_IMG_8714.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223181634_IMG_8712.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223181739_IMG_8717.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223181641_IMG_8713.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223181730_IMG_8716.JPG?10139439430536178035"
    ],
    "Alternate Gold":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/20170315171405_IMG_8984.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315171844_IMG_8991.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315171824_IMG_8989.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315171851_IMG_8992.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315171424_IMG_8988.JPG?10139439430536178035"
    ]
}
imgsTT={
    "White Home":[

    ],
    "Red Wine":[

    ],
    "Christmas '16":[

    ],
    "Alternate Gold":[

    ]
}
imgsJR={
    "White Home":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/Smith_White_Front.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Smith_White_Back.JPG?13313192378586356337",
    ],
    "Red Wine":[

    ],
    "Christmas '16":[

    ],
    "Alternate Gold":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/Smith_Gold_Front.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Smith_Gold_Back.JPG?13313192378586356337",
    ]
}
whichImages={
    "LeBron": imgsLBJ,
    "Kevin": imgsKL,
    "Kyrie": imgsKI,
    "Tristan": imgsTT,
    "JR" :imgsJR
}
with open("cle.csv", "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')

        headers =["Handle", "Title","Body (HTML)","Vendor","Type","Tags","Published", "Option1 Name", "Option1 Value", "Option2 Name","Option2 Value","Option3 Name", "Option3 Value","Variant SKU","Variant Grams","Variant Inventory Tracker","Variant Inventory Qty", "Variant Inventory Policy","Variant Fulfillment Service", "Variant Price",
        "Variant Compare At Price","Variant Requires Shipping","Variant Taxable","Variant Barcode","Image Src","Image Position","Image Alt Text","Gift Card","SEO Title","SEO Description","Google Shopping / Google Product Category","Google Shopping / Gender", "Google Shopping / Age Group","Google Shopping / MPN","Google Shopping / AdWords Grouping","Google Shopping / AdWords Labels",
        "Google Shopping / Condition","Google Shopping / Custom Product","Google Shopping / Custom Label 0","Google Shopping / Custom Label 1","Google Shopping / Custom Label 2","Google Shopping / Custom Label 3","Google Shopping / Custom Label 4","Variant Image","Variant Weight Unit","Variant Tax Code"]
        print len(headers)
        print sc30.firstName
        writer.writerow(headers)
        sizes=["S","M","L","XL","XXL"]
        players = [sc30,kt11,dg23,kd35]
        playerstack=[]
        for player in players:
            playerstack.append(player)

        for playerhandle in players:

            colorwaystack=[]
            for colorway in playerhandle.colorways:
                colorwaystack.append(colorway)
            toWrite=[None]*100
            for colorwayhandle in playerhandle.colorways:
                first=True;
                i=0
                #populate all images
                allImages=[]
                for img in whichImages[playerhandle.firstName][colorwayhandle]:
                    allImages.append(img)
                for img in totalImages:
                    if img not in allImages:
                        allImages.append(img)
                for size in sizes:

                    for colorway in colorwaystack:

                        for player in playerstack:
                            toWrite=[None]*100
                            if first==True:

                                title = playerhandle.teamName + " #"+str(playerhandle.playerNo)+" "+playerhandle.firstName+" "+playerhandle.lastName + " NBA Swingman Jersey"
                                toWrite[1]=title #title
                                toWrite[3]="Buckets.SG" #vendor
                                toWrite[4]="Jersey" #type
                                toWrite[7]="Size" #option1
                                toWrite[9]="Colorway" #option2
                                toWrite[11]= "Player" #option3
                            #loop over colorway and size

                            handle= playerhandle.teamAbbrev + "-" +playerhandle.firstName+"-"+ playerhandle.lastName+"-"+ colorwayhandle.split(' ', 1)[0]
                            toWrite[0]=handle.lower() #handle



                            toWrite[8]=size #option1value

                            toWrite[10]= colorway #option2value

                            toWrite[12]= player.firstName +" "+player.lastName+" #"+str(player.playerNo) #option3value
                            if player.playerNo >=10:
                                toWrite[13]= (player.teamAbbrev+colorway[0]+colorway[1]+colorway[2]+str(player.playerNo)+size).upper() #sku
                            else:
                                toWrite[13]= (player.teamAbbrev+colorway[0]+colorway[1]+colorway[2]+"0"+str(player.playerNo)+size).upper() #sku
                            toWrite[14]="250"
                            toWrite[15]="shopify"
                            toWrite[16]="1"
                            toWrite[17]="continue"
                            toWrite[18]="manual"
                            toWrite[19]="30"
                            toWrite[21]="TRUE"
                            toWrite[22]="TRUE"

                            #all images
                            if i<len(allImages):
                                toWrite[24]=allImages[i]
                                toWrite[25]=str(i+1)
                                i+=1

                            #variant images
                            try:
                                toWrite[43]=whichImages[player.firstName][colorway][0]
                            except IndexError:
                                print("no picture for"+colorway+player.firstName)

                            toWrite[44]="kg"
                            writer.writerow(toWrite)
                            first=False;
                first=True;
                colorwaystack.pop(0)
                colorwaystack.append(colorwayhandle)
            playerstack.pop(0)
            playerstack.append(playerhandle)
