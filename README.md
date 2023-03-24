# GPT1984
**Watch this repo to receive updates about this project**

GPT1984 allows the free use of GPT-3/4 thanks to the sharing of api-keys by people who decide to contribute

To share an api-key go via Tor Browser to the site **`kt4hxpyrz2fisyuxvdog6pbn5jgygjabc4xnly4psz3fzobso7uafoyd.onion`** and fill out the form, or send a request directly: `kt4hxpyrz2fisyuxvdog6pbn5jgygjabc4xnly4psz3fzobso7uafoyd.onion/share.php?api_key=<API-KEY-HERE>&key_type=GPT3-only`

key-type can be of two types: `GPT3-only` or `GPT4` . Choose the type depending on whether your apikey only supports GPT-3 or also GPT-4

Sharing the api-key will fail if:

1) the api-key already exists inside the system
2) the shared api-key is not a valid api-key
3) if both `api_key` and `key_type` parameters are not specified
4) if `key_type` is not equal to `GPT3_only` or `GPT4`

## When will GPT1984 launch? and how does it work?


the client will start working automatically only when the number of shared api-keys is equal to or greater than 200 (You can view the total number of the api-key already shared here: **`kt4hxpyrz2fisyuxvdog6pbn5jgygjabc4xnly4psz3fzobso7uafoyd.onion`**)

Before that, the client will be deactivated and no api-keys will be used. This is to avoid them all being drained in a short time and the reason is simple: to send the response to the prompt sent by the user, the client uses a different api-key for each single request, chosen randomly from the total list of api- shared keys in the system so the more api-keys there are in the system, the less each api-key will be used. Practically if a large number of api-keys are shared, the usage and expense for each api-keys will be very low since the probability that the same api-key will be used several times in a row is low! moreover, if an apikey is used, it could be added to the "recently used" list so as to be discarded from immediately following requests. This could allow a simple and fluid system to use GPT-3 and 4 for free with a very small expense for those who decide to contribute an api-key!


