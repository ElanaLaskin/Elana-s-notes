class Lesson:
    pass

master_list = []

lesson1_1 = Lesson()
lesson1_1.header = 'Lesson 1.1 The Basics of the Web and HTML'
lesson1_1.bullets = ['the web is written in HTML.',
'HTML=HyperText Markup Language', 'HTTP communicates between browser and servers.',
'2 types of tags in HTML: <br>A) &lt;p&gt; &lt;/p&gt; B) &lt;br&gt; (void tags)',
'element = content of the opening and closing tags', 'inline and block']
lesson1_1.anchor = 'lesson1-1'
master_list.append(lesson1_1)

lesson1_2 = Lesson()
lesson1_2.header = 'Lesson 1.2 Creating a Structured Document'
lesson1_2.bullets = ['HTML controls the structure of the web CSS controls the style.',
'''HTML is made up of tree like structures or parent-child relationships. This is the
attribute of nestled elements. This means that one HTML element has the ability to contain
more elements. The indentation in the code indicates this nesting. The more indented the item
 is, the more it is nested inside other elements. <a href="https://www.udacity.com/course/
 viewer#!/c-nd000/l-4137489485/e-2771378561/m-2771378562">This</a> video on Udacity does a
  good job in explaining this idea.''',
'''When veiwing the code in the browser's developer tools, the sideways triangles are HTML
element that have opening and closing tags.''',
'All shapes and texts are really boxes.']
lesson1_2.anchor = 'lesson1-2'
master_list.append(lesson1_2)

lesson1_3 = Lesson()
lesson1_3.header = 'Lesson 1.3 Adding CSS Style and HTML Structure'
lesson1_3.bullets = ['CSS = Cascading Style Sheets',
'In HTML, div is used for blocks and span for inline. Classes are for similar types and "id" is for more specific. Avoid using "id" a lot.', '''Good organization and structure
in the HTML means less repetition in the CSS. Avoiding repetition is a key component in
programming for many reasons.''', 'It allows programmers to save time and develope their code more efficiently.',
'Programmers can avoid copy and paste errors and other syntactic mistakes.', 'Programmers can maintain their code more effectively.']
lesson1_3.anchor = 'lesson1-3'
master_list.append(lesson1_3)

lesson4_1 = Lesson()
lesson4_1.header = 'Lesson 4.1 Introduction to Networks'
lesson4_1.bullets = ['''Network = a group of entities that can communicate,
even though they are not directly connected.''', '''Latency = the time it takes message to get
from source to destination. It's measured in milliseconds.''', '''Bandwith = amount of information
that can be transmitted per unit time. It's measured in mbps, mega bits per second.''', '''Bit =
smallest unit of information. It's represented as 0 or 1. Everything can be represented as such
when it's broken down enough.''', '''Protocols = rules of "communication" between client (web
browser) and server (Udacity). The protocol used is Hypertext Transfer Protocol, HTTP. The client
sends a message to the server to get a specified address. This is what your url is.''']
lesson4_1.anchor = 'lesson4-1'
master_list.append(lesson4_1)

lesson4_2 = Lesson()
lesson4_2.header = 'Lesson 4.2 Make the Internet Work for You'
lesson4_2.bullets = ['''Let's break down the URL (Uniform Resource Locator): "http://www.udacity.com/course/viewer#!/c-nd000"''',
 '  "http" = protocol', '   "www.udacity.com" = host / server', '   "course/viewer#!/c-nd000" = path, location of specific doc.'
'''Query Parameters (GET parameters) = extra information for the server in the path location.
The format is name = value. The query parameter is preceded with a "?" and additional query
parameters are added after "&" symbol.''', '''Fragment = usually locates a specific part of the
page. The fragment isn't sent to the server, it stays in the web browser. The fragment is preceded
by a "#".''', '''How does a server handle a request?''', 'First, the client contacts the server (www.udacity.com)',
'''Now there is a request line for the server. The request line has: a method (GET), a path (course/viewer), and a version (http 1.1 or 1.0) The request line looks like this: "GET /course HTTP/1.1"
''', '''Next, there is a response line from the server called status or dynamic. Static is a pre-written file like an image. Dynamic is content made on the fly. This is where web applications come in. A web app is a program that generates content.
''', 'The status line has:', 'a version identical to the request line', 'status code beginning with 1,2,3,4,5', '2- - means doc was found', '3- - means doc is located somewhere else', '''4- - means doc wasn't found, error on browser side''',
'5- - means server broke with this, error on server end']
lesson4_2.anchor = 'lesson4-2'
master_list.append(lesson4_2)

lesson4_4 = Lesson()
lesson4_4.header = 'Lesson 4.4 Python Break - Modulus & Dictionaries'
lesson4_4.bullets = ['Modulus Operator (%) = remainder of division',
'Dictionary = a set of key, value pairs']
lesson4_4.anchor = 'lesson4-4'
master_list.append(lesson4_4)

lesson4_6 = Lesson()
lesson4_6.header = 'Lesson 4.6 Validation'
lesson4_6.bullets = ['''Validation means verifying that user input is what is expected. Servers can
"receive junk", and the server has to be able to handle it both for security purposes and to
maintain positive user experience. Without validation, a user can maliciously enter code into
a form and thereby break into the server's program. Validation also allows the server to interpret
the input and respond accordingly. ''', 'What happens?', 'First, the user requests a form (get)',
'Then, the server supplies form', 'Next. the user replies (post)', 'Finally, the server verifies post and either accepts post or sends form again with error message.']
lesson4_6.anchor = 'lesson4-6'
master_list.append(lesson4_6)

lesson4_7 = Lesson()
lesson4_7.header = 'Lesson 4.7 HTML Templates'
lesson4_7.bullets = ['''A template is a way to build complicated strings (usually in HTML). We use a
template library as a source of templates.''', 'Why are templates important?', 'organizes code and allows editor to highlight syntax',
'Allows separation of different type of code', 'easily mutable', 'less error prone', 'Avoids repetition.'
'''All the above attributes are always essential in programming, as they conserve programers' time and effort.''',
'How to incorporate the template into our code:', 'First add the library to the app engine page.',
'Then import the library on main page.', 'Next define location  of template by concatenating the current file location and the word "templates".',
 'Finally use this defined directory to load template library with a file system loader.']
lesson4_7.anchor = 'lesson4-7'
master_list.append(lesson4_7)

submit_comments = Lesson()
submit_comments.header = 'Comments'
submit_comments.anchor = 'submit_comments'
master_list.append(submit_comments)