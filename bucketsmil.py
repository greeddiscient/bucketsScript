import csv

class player(object):
    def __init__(self,firstName,lastName, teamName,teamAbbrev,playerNo,colorways):
        self.firstName=firstName
        self.lastName=lastName
        self.teamName=teamName
        self.teamAbbrev=teamAbbrev
        self.playerNo=playerNo
        self.colorways=colorways

sc30=player("Jabari", "Parker", "Milwaukee Bucks", "mil", 12,["White Home","Green Away","Alternate Black"])
kt11=player("Giannis", "Antetokounmpo", "Milwaukee Bucks", "mil", 34,["White Home","Green Away","Alternate Black"])
# dg23=player("Kevin", "Love", "Cleveland Cavaliers", "cle", 0,["White Home","Red Wine","Alternate Gold","Christmas '16'"])
# kd35=player("JR", "Smith", "Cleveland Cavaliers", "cle", 5,["White Home","Red Wine","Alternate Gold","Christmas '16'"])
# ai09=player("Tristan", "Thompson", "Cleveland Cavaliers", "cle", 13,["White Home","Red Wine","Alternate Gold","Christmas '16'"])


totalImages=[
    "https://cdn.shopify.com/s/files/1/2019/6095/files/20170223175003_IMG_8665.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223174751_IMG_8663.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223175014_IMG_8666.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223174802_IMG_8664.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223175022_IMG_8667.JPG?10139439430536178035"
]

imgsJB={
    "White Home":[

    ],
    "Green Away":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/20170223175224_IMG_8670.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223175346_IMG_8675.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223175316_IMG_8674.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223175354_IMG_8676.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223175248_IMG_8672.JPG?10139439430536178035"
    ],
    "Alternate Black":[

    ]
}

imgsGA={
    "White Home":[

    ],
    "Green Away":[

    ],
    "Alternate Black":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/20170223175003_IMG_8665.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223174751_IMG_8663.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223175014_IMG_8666.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223174802_IMG_8664.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223175022_IMG_8667.JPG?10139439430536178035"
    ]
}
whichImages={
    "Jabari": imgsJB,
    "Giannis": imgsGA
}



with open("mil.csv", "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')

        headers =["Handle", "Title","Body (HTML)","Vendor","Type","Tags","Published", "Option1 Name", "Option1 Value", "Option2 Name","Option2 Value","Option3 Name", "Option3 Value","Variant SKU","Variant Grams","Variant Inventory Tracker","Variant Inventory Qty", "Variant Inventory Policy","Variant Fulfillment Service", "Variant Price",
        "Variant Compare At Price","Variant Requires Shipping","Variant Taxable","Variant Barcode","Image Src","Image Position","Image Alt Text","Gift Card","SEO Title","SEO Description","Google Shopping / Google Product Category","Google Shopping / Gender", "Google Shopping / Age Group","Google Shopping / MPN","Google Shopping / AdWords Grouping","Google Shopping / AdWords Labels",
        "Google Shopping / Condition","Google Shopping / Custom Product","Google Shopping / Custom Label 0","Google Shopping / Custom Label 1","Google Shopping / Custom Label 2","Google Shopping / Custom Label 3","Google Shopping / Custom Label 4","Variant Image","Variant Weight Unit","Variant Tax Code"]
        writer.writerow(headers)
        sizes=["S","M","L","XL","XXL"]
        players = [sc30,kt11]
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
