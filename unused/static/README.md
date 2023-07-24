#### About
The files inside this directory are unused openai static files.
The difference between these static files and the static files currently used is **plugin is prompt on almost any islam related question**

To summarize the differences:
- Unused files can prompt the plugin on almost any Islam related question, while current files only prompt if user asks about hadiths related to the question. This is due to the way the plugin description is written (mentions answering users using an islamic knowledge base while current files do not mention that)

#### Example
Using the current files, if the user prompts chat gpt using the below text:
`How should one marry in islam?`
The plugin would not be prompted, because there is no mention of the use asking about hadiths.

But using the unused files, if the user asks the same question the plugin will be prompted.


#### Reason for keeping
This was a product choice where we needed to choose whether we would want the plugin usage to be more or less enforced.
We decided to make it less enforced. Since we believed that the plugin should only do what it says it does and that is returning a list of hadiths for the user.