// const { sprintf } = require("sprintf")

(async ()=>{
    global.log = console.log.bind(console)
    puppeteer = require('puppeteer')


    path = require("path")
    fs = require("fs")
    sprintf = require("sprintf")
    sleep = require("await-sleep")
    random = require("random-number")

    seed = "https://www.balticshipping.com/vessel/imo/"
    urls =[]

    filepath = path.join(__dirname, "order-imo-list.txt")
    imoList = fs.readFileSync(filepath).toString().split('\n')
    imoList.forEach((imo, index, array)=>{
        urls.push(seed+imo)
    })

    seletorList=[]

    for(i of [1,2,3,5,7,8,9,12,13,14]){
        sel = {}


        sel.title = sprintf('#vessel_info > div:nth-child(1) > div > div.ship-info-container > table > tbody > tr:nth-child(%d) > %s', i, 'th')
        sel.value = sprintf('#vessel_info > div:nth-child(1) > div > div.ship-info-container > table > tbody > tr:nth-child(%d) > %s', i, 'td')
        seletorList.push(sel)
    }


    // console.log(seletorList)
    try{
        // console.log(puppeteer)

        browser = await puppeteer.launch()

        page = await browser.newPage()
        shipList = []

        await page.goto(urls[0])
        ship = []
        for(sel of seletorList){
            obj = {}
            obj.title = await page.$eval(sel.title, (el)=> el.textContent)
            obj.value = await page.$eval(sel.value, (el)=> el.textContent)
            ship.push(obj)
        }
        log(ship)

        fs.writeFileSync('ship-info.json', JSON.stringify(ship, null, 2))
        await browser.close()

    }catch(e){
        console.log(e)
    }




    
})()




