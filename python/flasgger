#Flasgger
## Acessando Swagger:
> go to: http://localhost:<port>/apidocs/

## Documentação em arquivo separado:
- Python Code (Flask)
```python
from flask import Blueprint, json, request, Response
from flasgger import swag_from

@financialAnalisysApi.route("/tickerinfo/<ticker>", methods=["GET"])
@swag_from('docs/get_ticker_info.yml')
def get_ticker_info(ticker):
    if not _ticker_exists(ticker):
```
- Swagger File (YAML) (one file per route)
```
Gets information for a ticker (such as volume, highprices, etc.), minute by minute. Can be limited by a range of dates.
     ---
     parameters:
      - name: ticker 
        description: Ticker identification in stock exchange
        example: BBDC3
        in: path          
        required: true
        schema:      
         type: string 
      - name: startDate
        description:
         Start day for the query
        example: '01-01-2001'
        in: query        
        required: false
        schema:
         type: string
         pattern: '^\d{2}-\d{2}-\d{4}$'        
      - name: endDate
        description:
         End day for the query
        example: '01-01-2001'
        in: query        
        required: false
        schema:
         type: string
         pattern: '^\d{2}-\d{2}-\d{4}$'        
     definitions:
      tickerInfo:
       type: array
       items:
        type: object
        properties:
         closeprice: 
          type: number
         highprice:
          type: number
         lowprice:
          type: number
         openprice:
          type: number
         volume:
          type: integer
         time: 
          type: string 
      defaultResponse:
       type: object
       properties:
        succcess: 
         type: boolean
        result:
         $ref: '#/definitions/tickerInfo'
     responses:
      200:
       description: Returns a list of information about the requested ticker, minute by minute.
       schema:
        $ref: '#/definitions/defaultResponse'
       examples:
        json: {success: true, result:[{closeprice: 30.02, highprice: 30.14, lowprice: 30.01, openprice: 30.01, volume: 0, time: 'Mon, 02 Sep 2019 09:08:00 GMT' }]}
      400:
       description: Occurs when an incorrect input was passed when calling the api
      500:
       description: Server error
```

## Referências:
- [Documentação Flasgger](https://github.com/flasgger/flasgger)
