import csv

class player(object):
    def __init__(self,firstName,lastName, teamName,teamAbbrev,playerNo,colorways):
        self.firstName=firstName
        self.lastName=lastName
        self.teamName=teamName
        self.teamAbbrev=teamAbbrev
        self.playerNo=playerNo
        self.colorways=colorways

sc30=player("Chris", "Paul", "Los Angeles Clippers", "lac", 3,["White Home","Red Away","Black Alternate"])
kt11=player("Blake", "Griffin", "Los Angeles Clippers", "lac", 32,["White Home","Red Away","Black Alternate"])
dg23=player("Deandre", "Jordan", "Los Angeles Clippers", "lac", 6,["White Home","Red Away","Black Alternate"])
# kd35=player("JR", "Smith", "Cleveland Cavaliers", "cle", 5,["White Home","Red Wine","Alternate Gold","Christmas '16"])
# ai09=player("Tristan", "Thompson", "Cleveland Cavaliers", "cle", 13,["White Home","Red Wine","Alternate Gold","Christmas '16"])

totalImages=[
    "https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8337.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8340.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8338.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8341.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8339.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8345.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8345.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8345.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8347.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8346.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8355.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8349.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8357.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8350.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8358.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8359.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8363.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8360.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8361.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8376.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8366.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8369.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8367.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8370.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8368.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8374.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8372.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8375.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8373.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8376.JPG?10139439430536178035",

]

imgsCP={
    "White Home":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8337.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8340.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8338.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8341.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8339.JPG?10139439430536178035",
    ],
    "Red Away":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8359.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8363.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8360.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8361.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8376.JPG?10139439430536178035",
    ],
    "Black Alternate":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8374.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8372.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8375.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8373.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8376.JPG?10139439430536178035",
    ]
}

imgsBG={
    "White Home":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8345.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8345.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8345.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8347.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8346.JPG?10139439430536178035",
    ],
    "Red Away":[

    ],
    "Black Alternate":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8355.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8349.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8357.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8350.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8358.JPG?10139439430536178035",
    ]
}

imgsDJ={
    "White Home":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8366.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8369.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8367.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8370.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8368.JPG?10139439430536178035",
    ],
    "Red Away":[

    ],
    "Black Alternate":[

    ]
}
whichImages={
    "Chris": imgsCP,
    "Blake": imgsBG,
    "Deandre": imgsDJ,
}
with open("lac.csv", "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')

        headers =["Handle", "Title","Body (HTML)","Vendor","Type","Tags","Published", "Option1 Name", "Option1 Value", "Option2 Name","Option2 Value","Option3 Name", "Option3 Value","Variant SKU","Variant Grams","Variant Inventory Tracker","Variant Inventory Qty", "Variant Inventory Policy","Variant Fulfillment Service", "Variant Price",
        "Variant Compare At Price","Variant Requires Shipping","Variant Taxable","Variant Barcode","Image Src","Image Position","Image Alt Text","Gift Card","SEO Title","SEO Description","Google Shopping / Google Product Category","Google Shopping / Gender", "Google Shopping / Age Group","Google Shopping / MPN","Google Shopping / AdWords Grouping","Google Shopping / AdWords Labels",
        "Google Shopping / Condition","Google Shopping / Custom Product","Google Shopping / Custom Label 0","Google Shopping / Custom Label 1","Google Shopping / Custom Label 2","Google Shopping / Custom Label 3","Google Shopping / Custom Label 4","Variant Image","Variant Weight Unit","Variant Tax Code"]
        print len(headers)
        print sc30.firstName
        writer.writerow(headers)
        sizes=["S","M","L","XL","XXL"]
        players = [sc30,kt11,dg23]
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
