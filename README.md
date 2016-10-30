# Code2040
Code from my Code2040 Fellowship Application
>Tokens have been removed

## Stage 4 Challenges

The biggest challenge here was not the actual problem of filtering the array but 
figuring out how to submit it, specifically the problem of properly encoding the 
request for validation.  The question is asked a couple times in the FAQ, but 
essentially its the same question:
>"Why am I getting 400 errors and 'That's not the right response. Try again.' 
I know my answer is right but it's not being accepted.  What's up?"

I took a couple routes when trying to debug.  At first I thought, "Maybe its a 
string encoding issue related to me taking in unicode and converting it to 
python's own encodings".  Nope.  Then I tried adding headers to my request to 
specify that what I was sending was ```{'Content-Type' : 'application/json'}```. Nada.
Ultimately I decided to take a look at what I was actually POSTing.

Using www.httpbin.org, this really cool service for HTTP library testing, 
I looked at the payload I was sending:

This Code: ```r = requests.post("http://httpbin.org/post", data=params)```

Sends This:
```
{
  "args": {},
  "data": "",
  "files": {},
  "form": {
    "array": [
      "xvbpnakq",
      "dmfywcuj",
      "dycpzhau",
      "vxzeawgr",
      "onmxpgay",
      "wtfkgpjb",
      "agphtrzu",
      "zinmrfck",
      "qfevknhc"
    ],
    "token": "<token>"
  },
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "173",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.10.0"
  },
  "json": null,
  "origin": "<ip-address>",
  "url": "http://httpbin.org/post"
}
```
There is a lot of helpful information in there, but for now focus on the 
content-type, data and form keys.  Quoted from the Python Requests library docs:  
>"Typically, you want to send some form-encoded data — much like an HTML form. To do this, simply pass a dictionary to the data argument.  Your dictionary of data will automatically be form-encoded when the request is made"

Notice a couple things, the payload I'm sending is under the form key, the data 
key's value is empty, and the content type is``` 'application/x-www-form-urlencoded'```.
These things happened because Requests is guessing at how to put together the
things I'm sending in a coherent order.  However this time, unlike in Stage 1-3 
and 5, it's guessing wrong.  

It took me a while to find but, luckily, the Requests library has a way to tell 
it that what you're sending is JSON using (you'll never guess what it is...) 
the json parameter (I know right).

This Code: ```r = requests.post("http://httpbin.org/post", json=params)```

Sends This:
```
{
  "args": {},
  "data": "{\"token\": \"<token>\", \"array\": [\"naybujhm\", \"pilrzeus\", \"zcnwxmso\", \"szqvonkw\", \"wdtpreul\", \"inpsxltw\"]}",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "128",
    "Content-Type": "application/json",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.10.0"
  },
  "json": {
    "array": [
      "naybujhm",
      "pilrzeus",
      "zcnwxmso",
      "szqvonkw",
      "wdtpreul",
      "inpsxltw"
    ],
    "token": "<token>"
  },
  "origin": "<ip-address>",
  "url": "http://httpbin.org/post"
}
```
Now take another look.  The data key, the body of the request, is no longer empty 
but now holds a raw JSON string corresponding to the payload.  The form key is 
now empty.  The content-type is now ```'application/json'```, the correct type.  Also, 
we now have something new in the json key, our parsed data string.

This second format is what the server accepted, bringing my long search to an 
end.  Main Takeaways: be persistent and don't be afraid to dig DEEP into the 
documentation of whatever library your using, more often than not the answers 
are in there. 

P.S. Thanks for reading through all of this.  For your persistance, here is an 
ascii picture of a kitten the size of the palm of your hand.

                  .               ,.
                  T."-._..---.._,-"/|
                  l|"-.  _.v._   (" |
                  [l /.'_ \; _~"-.`-t
                  Y " _(o} _{o)._ ^.|
                  j  T  ,-<v>-.  T  ]
                  \  l ( /-^-\ ) !  !
                   \. \.  "~"  ./  /c-..,__
                     ^r- .._ .- .-"  `- .  ~"--.
                      > \.                      \
                      ]   ^.                     \
                      3  .  ">            .       Y  
         ,.__.--._   _j   \ ~   .         ;       |
        (    ~"-._~"^._\   ^.    ^._      I     . l
         "-._ ___ ~"-,_7    .Z-._   7"   Y      ;  \        _
            /"   "~-(r r  _/_--._~-/    /      /,.--^-._   / Y
            "-._    '"~~~>-._~]>--^---./____,.^~        ^.^  !
                ~--._    '   Y---.                        \./
                     ~~--._  l_   )                        \
                           ~-._~~~---._,____..---           \
                               ~----"~       \
                                              \
