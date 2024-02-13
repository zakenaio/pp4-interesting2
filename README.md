# [PP4 INTERESTING NEWS](https://pp4-interesting-736b0c86bab7.herokuapp.com)


Reasons for site. 


MULTI SCREENSHOT OF SITE. 
![screenshot](documentation/mockup.png)

## UX

IMAGE HOME
IMAGE MENU
IMAGE TOP
IMAGE ARTICLE
IMAGE COMMENT

### Colour Scheme

IMG COLOURS 

- `#000000` used for primary text.
- `#E84610` used for primary highlights.
- `#4A4A4F` used for secondary text.
- `#009FE3` used for secondary highlights.

Explain colours. 

### Typography

- Barlow. Link to google fonts!

- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer.

## User Stories



### New Site Users

- As a new site user, I would like to ____________, so that I can ____________.
- As a new site user, I would like to ____________, so that I can ____________.
- As a new site user, I would like to ____________, so that I can ____________.
- As a new site user, I would like to ____________, so that I can ____________.
- As a new site user, I would like to ____________, so that I can ____________.

### Returning Site Users

- As a returning site user, I would like to ____________, so that I can ____________.
- As a returning site user, I would like to ____________, so that I can ____________.
- As a returning site user, I would like to ____________, so that I can ____________.
- As a returning site user, I would like to ____________, so that I can ____________.
- As a returning site user, I would like to ____________, so that I can ____________.

### Site Admin

- As a site administrator, I should be able to ____________, so that I can ____________.
- As a site administrator, I should be able to ____________, so that I can ____________.
- As a site administrator, I should be able to ____________, so that I can ____________.
- As a site administrator, I should be able to ____________, so that I can ____________.
- As a site administrator, I should be able to ____________, so that I can ____________.

## Wireframes



### Mobile Wireframes

<details>
<summary> Click here to see the Mobile Wireframes </summary>

Home
  - ![screenshot](documentation/wireframes/mobile-home.png)

Top Rated
  - ![screenshot](documentation/wireframes/mobile-about.png)

Modal Sign Up 
  - ![screenshot](documentation/wireframes/mobile-gallery.png)

Modal Sign In
  - ![screenshot](documentation/wireframes/mobile-contact.png)

Modal Sign Out 
  - ![screenshot](documentation/wireframes/mobile-gallery.png)

Modal Create News 
  - ![screenshot](documentation/wireframes/mobile-gallery.png)

Modal Edit News
  - ![screenshot](documentation/wireframes/mobile-gallery.png)



</details>

### Tablet Wireframes

<details>
<summary> Click here to see the Tablet Wireframes </summary>

Home
  - ![screenshot](documentation/wireframes/tablet-home.png)

Top Rated
  - ![screenshot](documentation/wireframes/tablet-about.png)

Modal Sign Up 
  - ![screenshot](documentation/wireframes/tablet-gallery.png)

Modal Sign In
  - ![screenshot](documentation/wireframes/tablet-contact.png)

Modal Sign Out 
  - ![screenshot](documentation/wireframes/tablet-gallery.png)

Modal Create News 
  - ![screenshot](documentation/wireframes/tablet-gallery.png)

Modal Edit News
  - ![screenshot](documentation/wireframes/tablet-gallery.png)



</details>

### Desktop Wireframes

<details>
<summary> Click here to see the Desktop Wireframes </summary>

Home
  - ![screenshot](documentation/wireframes/desktop-home.png)

Top Rated
  - ![screenshot](documentation/wireframes/desktop-about.png)

Modal Sign Up 
  - ![screenshot](documentation/wireframes/desktop-gallery.png)

Modal Sign In
  - ![screenshot](documentation/wireframes/desktop-contact.png)

Modal Sign Out 
  - ![screenshot](documentation/wireframes/desktop-gallery.png)

Modal Create News 
  - ![screenshot](documentation/wireframes/desktop-gallery.png)

Modal Edit News
  - ![screenshot](documentation/wireframes/desktop-gallery.png)

</details>

## Features

Explain features. Why modals, etc. 

### Existing Features

- **Title for feature #1**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/feature01.png)


### Future Features

OpenGraph, and so on, more! 

- Title for future feature #1
    - Any additional notes about this feature.
- Title for future feature #2
    - Any additional notes about this feature.
- Title for future feature #3
    - Any additional notes about this feature.

## Tools & Technologies Used

Add to this.
- pydot - for ERD 
- ckeditor



- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [CSS Flexbox](https://www.w3schools.com/css/css3_flexbox.asp) used for an enhanced responsive layout.
- [CSS Grid](https://www.w3schools.com/css/css_grid.asp) used for an enhanced responsive layout.
- [JavaScript](https://www.javascript.com) used for user interaction on the site.
- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [GitHub Pages](https://pages.github.com) used for hosting the deployed front-end site.
- [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [Django](https://www.djangoproject.com) used as the Python framework for the site.
- [PostgreSQL](https://www.postgresql.org) used as the relational database management.
- [ElephantSQL](https://www.elephantsql.com) used as the Postgres database.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.
- [Cloudinary](https://cloudinary.com) used for online static file storage.
- [phind](https://www.phind.com/) used for tips and trix, a great way to make progress when stuck. 


## Database Design

```python
  CATEGORIES 
class Category(models.Model):
    """
    Represents a category for posts. Each category has a unique name,
    an optional description, and a publication date.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

NEW POSTS
class News_Post(models.Model):
    """
    Represents a news post. Each post has a title, rich text content,
    an author, an category, optional image, a publication date,
    and a vote count.
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True, unique=True)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = CloudinaryField(
        'image', default=None, null=True, blank=True
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)

    class Meta:
        db_table = 'news_post'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            # Unique slug,
            unique_slug = self.slug
            num = 1
            while News_Post.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{self.slug}-{num}'
                num += 1
            self.slug = unique_slug
        super(News_Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

COMMENTS
class Comment(models.Model):
    """
    Represents a comment on a post. Each comment is linked to a post, may have
    an author name (if the author is unauthenticated), contains text, and has a
    publication date.
    """
    post = models.ForeignKey(News_Post, related_name='comments', on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100, blank=False, null=True)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author_name or 'Anonymous'} on {self.post.title}"

FORM for COMMENTS
class CommentForm(forms.ModelForm):
    """
    A Django form for creating and editing comments.
    """
    class Meta:
        model = Comment
        exclude = ['post']

PROFILES for USER for USER IMAGE
class Profile(models.Model):
    """
    Represents a user profile.
    Each profile is linked to a user and has an avatar image.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = CloudinaryField(
        'image',
        default='avatar',
    )

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
```

![ERD](documentation/erd.png)

User:
News_Post: One User can author many News_Posts through a foreign key relationship.
Profile: One User can have one Profile through a one-to-one relationship.
Comment: One User can write comments on many News_Posts (indirect connection through the News_Post model).

Category:
News_Post: Many News_Posts can belong to one Category through a foreign key relationship.

News_Post:
User: One News_Post is written by one User (author foreign key).
Category: One News_Post can belong to one Category (optional).
Comment: One News_Post can have many Comments through a foreign key relationship.

Comment:
News_Post: One Comment belongs to one News_Post (foreign key).
User: One Comment can be written by a User (indirect connection through the News_Post model).

Profile:
User: One Profile belongs to one User (one-to-one relationship).

Entities:

User: Represents a user of the system.
Attributes: id (primary key), username, email, password (hashed), profile (foreign key to Profile).
Profile: Represents a user's profile information.
Attributes: id (primary key), user (one-to-one relationship with User), avatar_url (Cloudinary image URL).
Category: Represents a category for posts.
Attributes: id (primary key), name (unique), description, pub_date.
News_Post: Represents a news post.
Attributes: id (primary key), title, slug (unique), content (HTML text with Cloudinary image URLs), author (foreign key to User), category (foreign key to Category), pub_date, votes.
Comment: Represents a comment on a post.
Attributes: id (primary key), post (foreign key to News_Post), author_name, text, pub_date.
Relationships:

One-to-one: User to Profile
One-to-many:
User to News_Post
Category to News_Post
News_Post to Comment
Many-to-one:
News_Post to Category
Comment to News_Post

## Agile Development Process

This is hard, this is almost harder than ERD. Spend two days. 

### GitHub Projects

[GitHub Projects](https://github.com/zakenaio/pp4-interesting2/projects) served as an Agile tool for this project.
It isn't a specialized tool, but with the right tags and project creation/issue assignments, it can be made to work.

Through it, user stories, issues, and milestone tasks were planned, then tracked on a weekly basis using the basic Kanban board.

![screenshot](documentation/gh-projects.png)

### GitHub Issues

[GitHub Issues](https://github.com/zakenaio/pp4-interesting2/issues) served as an another Agile tool.
There, I used my own **User Story Template** to manage user stories.

It also helped with milestone iterations on a weekly basis.

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Consider adding a screenshot of your Open and Closed Issues.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- [Open Issues](https://github.com/zakenaio/pp4-interesting2/issues)

    ![screenshot](documentation/gh-issues-open.png)

- [Closed Issues](https://github.com/zakenaio/pp4-interesting2/issues?q=is%3Aissue+is%3Aclosed)

    ![screenshot](documentation/gh-issues-closed.png)

### MoSCoW Prioritization

I've decomposed my Epics into stories prior to prioritizing and implementing them.
Using this approach, I was able to apply the MoSCow prioritization and labels to my user stories within the Issues tab.

- **Must Have**: guaranteed to be delivered (*max 60% of stories*)
- **Should Have**: adds significant value, but not vital (*the rest ~20% of stories*)
- **Could Have**: has small impact if left out (*20% of stories*)
- **Won't Have**: not a priority for this iteration

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://pp4-interesting-736b0c86bab7.herokuapp.com).

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:

- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: pp4-interesting2).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For *Primary interest*, you can choose *Programmable Media for image and video API*.
- Optional: *edit your assigned cloud name to something more memorable*.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user's own value |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | user's own value |

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/zakenaio/pp4-interesting2) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/zakenaio/pp4-interesting2.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/zakenaio/pp4-interesting2)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/zakenaio/pp4-interesting2)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

Local Development vs. Heroku Deployment: Key Differences

While developing and testing your application locally can be convenient, the environment is distinct from a live deployment setting like Heroku. Here's a breakdown of the key differences:

1. Logging:
Local: DEBUG mode is True, providing detailed error logs for easier troubleshooting.
Heroku: DEBUG is False to optimize performance and minimize security risks.


2. Database:
Local: You likely use a local database (e.g., SQLite) for convenience.
Heroku: Heroku's Postgres database offers a robust and managed solution for production use.


3. Sensitive Information:
Local: Sensitive data (e.g., SECRET_KEY, DATABASE_URL) might be stored in local configuration files.
Heroku: Store such information securely as environment variables in Heroku, accessible only to your application.


4. Static and Media Files:
Local: These files might be served directly from your local development environment.
Heroku: Services like Cloudinary and Whitenoise ensure efficient and secure delivery of static and media files in production.
By understanding these differences and making the necessary adjustments, you can ensure your application runs smoothly and securely on Heroku, providing a reliable and optimal experience for your users.



## Credits



### Content



| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://tim.2bn.dev/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [W3Schools](https://www.w3schools.com/howto/howto_js_topnav_responsive.asp) | entire site | responsive HTML/CSS/JS navbar |
| [StackOverflow](https://stackoverflow.com/) |  |  |
| [WhiteNoise](http://whitenoise.evans.io) | entire site | hosting static files on Heroku temporarily |

### Media

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Use this space to provide attribution links to any images, videos, or audio files borrowed from online.
A few examples have been provided below to give you some ideas.

If you're the owner (or a close acquaintance) of all media files, then make sure to specify this.
Let the assessors know that you have explicit rights to use the media files within your project.

Ideally, you should provide an actual link to every media file used, not just a generic link to the main site!
The list below is by no means exhaustive. Within the Code Institute Slack community, you can find more "free media" links
by sending yourself the following command: `!freemedia`.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [Pexels](https://www.pexels.com) | entire site | image | favicon on all pages |
| [Lorem Picsum](https://picsum.photos) | home page | image | hero image background |
| [Unsplash](https://unsplash.com) | product page | image | sample of fake products |
| [Pixabay](https://pixabay.com) | gallery page | image | group of photos for gallery |
| [Wallhere](https://wallhere.com) | footer | image | background wallpaper image in the footer |
| [This Person Does Not Exist](https://thispersondoesnotexist.com) | testimonials | image | headshots of fake testimonial images |
| [Audio Micro](https://www.audiomicro.com/free-sound-effects) | game page | audio | free audio files to generate the game sounds |
| [Videvo](https://www.videvo.net/) | home page | video | background video on the hero section |
| [TinyPNG](https://tinypng.com) | entire site | image | tool for image compression |

### Acknowledgements



- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for their support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) tutor team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and imposter syndrome.
- I would like to thank my partner (John/Jane), for believing in me, and allowing me to make this transition into software development.
- I would like to thank my employer, for supporting me in my career development change towards becoming a software developer.
