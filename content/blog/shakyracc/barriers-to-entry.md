title: Barriers To Entry
date: 2022-07-24
tags: blog
slug: barriers-to-entry

### 2022-07-24-07-05

Barriers to entry when updating the blog: 

- **it takes time**. i usually think “i’ll get to it later” but then obviously later comes and we’ve completely forgotten what it is we wanted to share. the whole point of this thing is to share a snapshot of thoughts, ideas and learnings. i’ve learned SOOOO many valuable lessons over the past 4 years and i want nothing more than to share them. on my own walk through life i’ve found it really hard to find resources that teach what i’ve learned, which made growing a lot more painful that it needed to be. …… SO, getting to it later is a ridiculous plan. that mindset is a barrier worth mentioning and holding myself accountable for.
- i’m never really sure if updating **github pages** will take 5 minutes or a day. i still don’t understand how much space to reserve for this process and the thought of slaving over the issue for more than 1 minutes turns me away.
- thinking about the **audience** kills the vibe immediately. i’ve found myself struck with ‘small island brain’ (or maybe ‘small town brain’?). This has to be a thing right? Where instead of thinking globally we think only of the people nearest us? Whenever I think about writting something, unfortunately i immediately think “what will jack and jill from down the road think?”. Which, when you examine it, is absolutely insane! Because why care about the opinions of individuals you wouldn’t take advice from?????? Gosh, I can’t wait to get over that mind hump.
- **perfectionism**. a classic. wanting to write the perfect blog post. feeling like i’m unable to express myself in a clear and concise way. *i just had a thought.* lol if no one is gonna read this blog anyway, why should it matter how it’s written. so what if it’s littered with scattered thoughts, run on sentences, grammatical errors…etc. the whole point of this thing is to share! the whole point of this thing is to toss the things i’m learning out into the ether in hopes of someone else finding it valuable some day.

listing these barriers out was a good exercise because i now see that only one of them is valid. the github pages issue can be fixed. it’ll take time, BUT it’s possible. and we’ll no doubt learn something from the solution and be able to share it here. boom.

this morning i shared a #morningthought in the hikes & friendship whatsapp group. it said: 
> Don’t ever stop yourself from trying something in fear of what people on this island will think.
> There is a HUGE world out there and someone, somewhere appreciates your efforts.
> Don’t let the bubble limit you. What you can do in this life is infinite.

<br>

anyway, let’s update this thing. seems like i’ve forgotten some of the terminal commands. let’s list them here.

1️⃣ to activate the virtualenv, navigate to the virtualenv directory using ` cd virtualenv ` and enter ` source /bin/activate `. i definitely had to hit the up arrow in terminal to get the entry history (i’m sure there’s a more technical way of saying that, bleh) to find that command. seems like terminal recalls the commands you’ve made in specific directories. cool… also, i know. i shouldn’t be using virtualenv with python3 but i didn’t know that at the time i created it. i should be using venv instead)

2️⃣ okay now i find the directory storing the blog posts, use `  touch filename.md ` to create a new markdown file and (i had to google this one) use ` open filename.md ` to open the file. honestly why didn’t i try that before going to google? #unimpressed '
   
the file opens in Xcode which is currently my favourite markdown editor. to be fair i’ve only used Xcode and VS Code for this, but Xcode feels more lightweight. VS Code feels like a commitment…does that make sense? but perhaps i should get used to vscode because of the integrated terminal…. hmmm. that’s a good selling point. 
   
okay just tried to run ` code —version ` in terminal and go this back
   
> -bash: code: command not found
   
ugh, now we’re getting into PATH stuff. i hate it here. 
   
found explanation here: [https://stackoverflow.com/a/46343212/19118606](https://stackoverflow.com/a/46343212/19118606) only took 1 minute to find. 
   
`code —version` now returns 1.69.0 ! Yay, that wasn’t painful at all actually. brilliant. 
   
okay where was i? yes, open the file in vscode using `code filename.md`.
   
initial thoughts: it’s not so bad… it still feels more cluttered than Xcode but let’s go with it. 

3️⃣ copy and past the post from notion to the markdown file. i’m drafting in notion because it’s my favorite project management/note taking tool for personal projects.

4️⃣ now to format the blogpost in markdown. i've forgotten how to do that too so i'm using [Markdown Guide](https://www.markdownguide.org/basic-syntax/) to help. 

google how to add post date and time. i'd like to add this to document how long it takes to get the post online from starting the draft. should also add an automated screen showing time spent. 

oh shit, i just remembered i made plans with my mechanic to work on the xtrail today. darn it. i was planning on building a project with django. ugh. oh well, we'll just learn about CV joints instead. that's fun too. anyway let's rush this post off, add automated timespent screen to the roadmap and be done with this. 

5️⃣ use [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) to preview post. 

6️⃣ use `make html` to ... update the output directory? i think that's what this does. 

7️⃣ use `make serve` to view the website at localhost:8000 in browser.

8️⃣ use ctrl + C to stop the server

okay i admint vscode is so much more efficient, but for some reason the emoji picker doesn't appear when i hit ctrl + cms + space.

9️⃣ i've forgotten how to update github pages so i'm using [How I Built This Site](https://pythonforundergradengineers.com/how-i-built-this-site-7.html) to help. 

use `git pull origin main` to i guess get the github repo. <br>
use `make html` and `make serve` to update the repo i guess. <br>
use `pelican content -s publishconf.py` to create published version of the site <br>
use `git add .` <br>
use `git commit -m "add barriers-to-entry.md"` <br>
use `git push origin main` <br>
use `ghp-import output` to post contents of the output directory to gh-pages branch <br>
use `git push -f origin gh-pages` <br> to push to gh-pages. this didn't take more than a second surprisingly. awesome. 



