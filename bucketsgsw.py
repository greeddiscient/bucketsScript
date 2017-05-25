import csv

class player(object):
    def __init__(self,firstName,lastName, teamName,teamAbbrev,playerNo,colorways):
        self.firstName=firstName
        self.lastName=lastName
        self.teamName=teamName
        self.teamAbbrev=teamAbbrev
        self.playerNo=playerNo
        self.colorways=colorways

sc30=player("Stephen", "Curry", "Golden State Warriors", "gsw", 30,["White Home","Blue Away","Christmas '16","Throwback Yellow"])
kt11=player("Klay", "Thompson", "Golden State Warriors", "gsw", 11,["White Home","Blue Away","Christmas '16","Throwback Yellow"])
dg23=player("Draymond", "Green", "Golden State Warriors", "gsw", 23,["White Home","Blue Away","Christmas '16","Throwback Yellow"])
kd35=player("Kevin", "Durant", "Golden State Warriors", "gsw", 35,["White Home","Blue Away","Christmas '16","Throwback Yellow"])
# ai09=player("Andre", "Iguodala", "Golden State Warriors", "gsw", 9,["White Home","Blue Away","Christmas '16","Throwback Yellow"])

totalImages=[
    "https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8546.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8549.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8547.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8550.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8548.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8576.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8579.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8577.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8580.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8578.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8564.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8574.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8568.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8573.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8565.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8557.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8562.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8560.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8563.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8559.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8551.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8555.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8553.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8556.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8552.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8538.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8541.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8540.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8543.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8539.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8530.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8536.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8531.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8537.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8534.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315170024_IMG_8961.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315170103_IMG_8967.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315170034_IMG_8963.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315170111_IMG_8968.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315170040_IMG_8964.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Green_White_Front.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Green_White_Back.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Durant_Yellow_Front.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Durant_Yellow_Back.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Durant_Yellow_Det.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Green_Christmas_Front.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Green_Christmas_Back.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Green_Blue_Front.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Green_Blue_Back.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Thompson_Yellow_Front.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Thompson_Yellow_Back.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Curry_Yellow_Front.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Curry_Yellow_Back.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Thompson_Christmas_Front.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Thompson_Christmas_Back.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Thompson_Christmas_Det1.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Thompson_Christmas_Det.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Durant_Christmas_Front.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Durant_Christmas_Back.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Durant_Christmas_Det.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Durant_Christmas_Det1.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223181856_IMG_8718.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223181935_IMG_8721.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223181900_IMG_8719.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223181940_IMG_8722.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223181904_IMG_8720.JPG?10139439430536178035",


]

imgsSC={
    "White Home":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8546.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8549.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8547.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8550.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8548.JPG?10139439430536178035",
    ],
    "Blue Away":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8576.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8579.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8577.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8580.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8578.JPG?10139439430536178035",
    ],
    "Christmas '16":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/20170223181856_IMG_8718.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223181935_IMG_8721.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223181900_IMG_8719.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223181940_IMG_8722.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170223181904_IMG_8720.JPG?10139439430536178035",
    ],
    "Throwback Yellow":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/Curry_Yellow_Front.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Curry_Yellow_Back.JPG?13313192378586356337",
    ]
}


imgsKT={
    "White Home":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8538.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8541.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8540.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8543.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8539.JPG?10139439430536178035",
    ],
    "Blue Away":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8557.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8562.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8560.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8563.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8559.JPG?10139439430536178035",
    ],
    "Christmas '16":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/Thompson_Christmas_Front.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Thompson_Christmas_Back.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Thompson_Christmas_Det1.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Thompson_Christmas_Det.JPG?13313192378586356337",
    ],
    "Throwback Yellow":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/20170315170024_IMG_8961.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315170103_IMG_8967.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315170034_IMG_8963.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315170111_IMG_8968.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/20170315170040_IMG_8964.JPG?10139439430536178035",
    ]
}


imgsDG={
    "White Home":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/Green_White_Front.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Green_White_Back.JPG?13313192378586356337",
    ],
    "Blue Away":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/Green_Blue_Front.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Green_Blue_Back.JPG?13313192378586356337",
    ],
    "Christmas '16":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/Green_Christmas_Front.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Green_Christmas_Back.JPG?13313192378586356337",
    ],
    "Throwback Yellow":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8551.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8555.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8553.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8556.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8552.JPG?10139439430536178035",
    ]
}
imgsKD={
    "White Home":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8530.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8536.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8531.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8537.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8534.JPG?10139439430536178035",
    ],
    "Blue Away":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8564.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8574.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8568.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8573.JPG?10139439430536178035",
"https://cdn.shopify.com/s/files/1/2019/6095/files/IMG_8565.JPG?10139439430536178035",
    ],
    "Christmas '16":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/Durant_Christmas_Front.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Durant_Christmas_Back.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Durant_Christmas_Det.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Durant_Christmas_Det1.JPG?13313192378586356337",
    ],
    "Throwback Yellow":[
        "https://cdn.shopify.com/s/files/1/2019/6095/files/Durant_Yellow_Front.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Durant_Yellow_Back.JPG?13313192378586356337",
"https://cdn.shopify.com/s/files/1/2019/6095/files/Durant_Yellow_Det.JPG?13313192378586356337",
    ]
}

whichImages={
    "Stephen": imgsSC,
    "Klay": imgsKT,
    "Draymond": imgsDG,
    "Kevin": imgsKD
    # "Andre" :imgsJR
}
with open("gsw.csv", "wb") as csv_file:
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
