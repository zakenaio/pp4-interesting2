# Testing

Return back to the [README.md](README.md) file.



## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

- If you are copying/pasting your HTML code, use this link: https://validator.w3.org/#validate_by_input
- (*recommended*) If you are using the live deployed site pages, use this link: https://validator.w3.org/#validate_by_uri

- https://validator.w3.org/nu/?doc=https%3A%2F%2Fzakenaio.github.io%2Fpp4-interesting2%2Findex.html

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](LINK TO W3VALIDATION) | ![screenshot](IMG URL) |  |
| Popular | [W3C](LINK TO W3VALIDATION) | ![screenshot](IMG URL) |  |
| Detail page | [W3C](LINK TO W3VALIDATION) | ![screenshot](IMG URL) |  |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | GitHub URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Link to CSS on GitHub](https://github.com/zakenaio/pp4-interesting2/blob/main/static/css/style.css) | ![screenshot](documentation/testing/valid-css.png) | Pass: No Errors |


### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| script.js | ![screenshot](documentation/testing/jshint.png) | |


### Python

`# noqa` = **NO Quality Assurance** used for some of the longer lines, to not break functionality.

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | GitHub URL | Screenshot | Notes |
| --- | --- | --- | --- |
| interesting/settings.py | URL | ![screenshot](documentation/testing/pep8-settings.png) | used # noqa for long lines on five places, all regarding long lines as secret-keys and such. |
| interesting/urls.py | URL | ![screenshot](documentation/testing/pep8-urls2.png) | used # noqa for long lines once.  |
| news/admin.py | URL | ![screenshot](documentation/testing/pep8-admin.png) |  |
| news/apps.py | URL | ![screenshot](documentation/testing/pep8-apps.png) |  |
| news/context_processors.py | URL | ![screenshot](documentation/testing/pep8-cont.png) |  |
| news/forms.py | URL | ![screenshot](documentation/testing/pep8-forms.png) | used # noqa for long lines once.  |
| news/models.py | URL | ![screenshot](documentation/testing/pep8-models.png) | used # noqa for long lines twice. Broke some of the functionality if i tried to split the lines. |
| news/urls.py | URL | ![screenshot](documentation/testing/pep8-urls.png) | used # noqa for long lines once. |
| news/views.py | URL | ![screenshot](documentation/testing/pep8-views.png) | used # noqa for long lines twice |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Popular News | Detail | Modals Signed out | Modals Signed In | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Edge Windows11 | ![Edge Win Home](documentation/testing/browsers/edgewinhome.jpg) | ![Edge Win Popular](documentation/testing/browsers/edgewinpop.jpg) | ![Edge Win Detail](documentation/testing/browsers/edgewindetail.jpg) | ![Edge Win Sign Up Modal](documentation/testing/browsers/edgewinup.png) ![Edge Win Sign in  Modal](documentation/testing/browsers/edgewinin.png) | ![Edge Win Sign out Modal](documentation/testing/browsers/edgewinout.jpg) ![Edge win Create Modal](documentation/testing/browsers/edgewincreate.jpg) ![Edge win Edit Modal](documentation/testing/browsers/edgewinedit.png) | Works as expected |
| Brave Windows11 | ![Brave Win Home](documentation/testing/browsers/bravewinhome.jpg) | ![Brave Win Popular](documentation/testing/browsers/bravewinpop.jpg) | ![Brave Win Detail](documentation/testing/browsers/bravewindetail.jpg) | ![Brave Win Sign up Modal](documentation/testing/browsers/bravewinup.jpg) ![Brave Win Sign in Modal](documentation/testing/browsers/bravewinin.jpg) | ![Brave Win Sign out Modal](documentation/testing/browsers/bravewinout.png) ![Brave Win Create Modal](documentation/testing/browsers/bravewincreate.jpg) ![Brave win Edit Modal](documentation/testing/browsers/bravewinedit.png) | Works as expected |
| Safari macOS | ![Safari Home](documentation/testing/browsers/safarimachome.png) | ![Safari Popular](documentation/testing/browsers/safarimacpop.png) | ![Safari Detail](documentation/testing/browsers/safarimacdetail.png) | ![Safari Sign up Modal](documentation/testing/browsers/safarimacup.png) ![Safari Sign in Modal](documentation/testing/browsers/safarimacin.png) | ![Safari Sign out Modal](documentation/testing/browsers/safarimacout.png) ![Safari Create Modal](documentation/testing/browsers/safarimaccreate.png) ![Safari Edit Modal](documentation/testing/browsers/safarimacedit.png) | Works as expected |
| Brave macOS | ![Brave macOS Home](documentation/testing/browsers/bravemachome.png) | ![Brave macOS Popular](documentation/testing/browsers/bravemacpop.png) | ![Brave macOS Detail](documentation/testing/browsers/bravemacdetail.png) | ![Brave macOS Sign up Modal](documentation/testing/browsers/bravemacup.png) ![Brave macOS Sign in Modal](documentation/testing/browsers/bravemacin.png) | ![Brave macOS Sign out Modal](documentation/testing/browsers/bravemacout.png) ![Brave macOS Create Modal](documentation/testing/browsers/bravemaccreate.png) ![Brave macOS Edit Modal](documentation/testing/browsers/bravemacedit.png) | Works as expected |
| FireFox Linux | ![FireFox Linux Home](documentation/testing/browsers/fflinuxhome.png) | ![FireFox Linux Popular](documentation/testing/browsers/fflinuxpop.png) | ![FireFox Linux Detail](documentation/testing/browsers/fflinuxdetail.png) | ![FireFox Linux Sign up Modal](documentation/testing/browsers/fflinuxup.png) ![FireFox Linux Sign in Modal](documentation/testing/browsers/fflinuxin.png) | ![FireFox Linux Sign out Modal](documentation/testing/browsers/fflinuxout.png) ![FireFox Linux Create Modal](documentation/testing/browsers/fflinuxcreate.png) ![FireFox Linux Edit Modal](documentation/testing/browsers/fflinuxedit.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Home | Popular | Footer | Details | Modal | Modal | Modal |
| --- | --- | --- | --- | --- | --- | --- |
| **Desktop 1440p** |  |  |  |  |  |  |
| ![screenshot](documentation/testing/comp/desktophome.png) | ![screenshot](documentation/testing/comp/desktoppop.png) | ![screenshot](documentation/testing/comp/desktopfooter.png) | ![screenshot](documentation/testing/comp/desktopdetail.png) | ![screenshot](documentation/testing/comp/desktopcreate.png) | ![screenshot](documentation/testing/comp/desktopedit.png) | ![screenshot](documentation/testing/comp/desktopsignup.png) |
| Notes |  |  |  |  |  |  |
| **Macbook 16"** |  |  |  |  |  |  |
| ![screenshot](documentation/testing/comp/mavbookhome.png) | ![screenshot](documentation/testing/comp/macbookpop.png) | ![screenshot](documentation/testing/comp/macbookfooter.png) | ![screenshot](documentation/testing/comp/macbookdetail.png) | ![screenshot](documentation/testing/comp/macbookcreate.png) | ![screenshot](documentation/testing/comp/macbookpedit.png) | ![screenshot](documentation/testing/comp/macbooksignup.png) |
| Notes |  |  |  |  |  |  |
| **Tablet DEV** |  |  |  |  |  |  |
| ![screenshot](documentation/testing/comp/tabletdevhome.png) | ![screenshot](documentation/testing/comp/tabletdevpop.png) | ![screenshot](documentation/testing/comp/tabletdevfooter.png) | ![screenshot](documentation/testing/comp/tabletdevdetail.png) | ![screenshot](documentation/testing/comp/tabletdevcreate.png) | ![screenshot](documentation/testing/comp/tabletdevedit.png) | ![screenshot](documentation/testing/comp/tabletdevsignup.png) |
| Notes |  |  |  |  |  |  |
| **Pixel 3 DEV** |  |  |  |  |  |  |
| ![screenshot](documentation/testing/comp/pixel3home.png) | ![screenshot](documentation/testing/comp/pixel3pop.png) | ![screenshot](documentation/testing/comp/pixel3footer.png) | ![screenshot](documentation/testing/comp/pixel3detail.png) | ![screenshot](documentation/testing/comp/pixel3create.png) | ![screenshot](documentation/testing/comp/pixel3edit.png) | ![screenshot](documentation/testing/comp/pixel3signup.png) |
| Notes |  |  |  |  |  |  |
| **iPhone X DEV** |  |  |  |  |  |  |
| ![screenshot](documentation/testing/comp/iphonexhome.png) | ![screenshot](documentation/testing/comp/iphonexpop.png) | ![screenshot](documentation/testing/comp/iphonexfooter.png) | ![screenshot](documentation/testing/comp/iphonexdetail.png) | ![screenshot](documentation/testing/comp/iphonexcreate.png) | ![screenshot](documentation/testing/comp/iphonexedit.png) | ![screenshot](documentation/testing/comp/iphonexsignup.png) |
| Notes |  |  |  |  |  |  |
| **Devtools Small**  |  |  |  |  |  |  |
| ![screenshot](documentation/testing/comp/devsmallhome.png) | ![screenshot](documentation/testing/comp/devsmallpop.png) | ![screenshot](documentation/testing/comp/devsmallfooter.png) | ![screenshot](documentation/testing/comp/devsmalldetail.png) | ![screenshot](documentation/testing/comp/devsmallcreate.png) | ![screenshot](documentation/testing/comp/devsmalledit.png) | ![screenshot](documentation/testing/comp/devsmallsignup.png) |
| Notes |  |  |  |  |  |  |
| **Devtools Medium** |  |  |  |  |  |  |
| ![screenshot](documentation/testing/comp/devmediumhome.png) | ![screenshot](documentation/testing/comp/devmediumpop.png) | ![screenshot](documentation/testing/comp/devmediumfooter.png) | ![screenshot](documentation/testing/comp/devmediumdetail.png) | ![screenshot](documentation/testing/comp/devmediumcreate.png) | ![screenshot](documentation/testing/comp/devmediumedit.png) | ![screenshot](documentation/testing/comp/devmediumsignup.png) | 
| Notes |  |  |  |  |  |  |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

Problem with Lighthouse Audit with cloudinary not using https 
https://stackoverflow.com/questions/51884586/force-cloudinary-urls-to-use-https
https://community.cloudinary.com/discussion/484/my-urls-are-returned-in-the-http-instead-of-https

### Mobile
| Home | ![screenshot](documentation/testing/lighthouse/lh-mobile-home.png) |  |  |
| --- | --- | --- | --- |
| ![screenshot](documentation/testing/lighthouse/lh-mobile-home-perfomance.png) | ![screenshot](documentation/testing/lighthouse/lh-mobile-home-access.png) | ![screenshot](documentation/testing/lighthouse/lh-mobile-home-bestpract.png) | ![screenshot](documentation/testing/lighthouse/lh-mobile-home-SEO.png) |
| issues mostly based on heroku | minor issues | issues based on cloudinary | issues based on trigging modals, and robots.txt |

| Popular News | ![screenshot](documentation/testing/lighthouse/lh-mobile-pop.png) |  |  |
| --- | --- | --- | --- |
| ![screenshot](documentation/testing/lighthouse/lh-mobile-pop-perfomance.png) | ![screenshot](documentation/testing/lighthouse/lh-mobile-pop-access.png) | ![screenshot](documentation/testing/lighthouse/lh-mobile-pop-bestpract.png) | ![screenshot](documentation/testing/lighthouse/lh-mobile-pop-SEO.png) |
| Same heroku, some minor about using jpg/png and not next gen | minor issues | issues based on cloudinary | issues based on trigging modals, and robots.txt |

| News Detail | ![screenshot](documentation/testing/lighthouse/lh-mobile-detail.png) |  |  |
| --- | --- | --- | --- |
| ![screenshot](documentation/testing/lighthouse/lh-mobile-detail-perfomance.png) | ![screenshot](documentation/testing/lighthouse/lh-mobile-detail-access.png) | ![screenshot](documentation/testing/lighthouse/lh-mobile-detail-bestpract.png) | ![screenshot](documentation/testing/lighthouse/lh-mobile-detail-SEO.png) |
| More of the same | minor issues, some i can not understand. Flags bootstrap elements, but ok score | same cloudinary https issues | issues based on trigging modals, and robots.txt |


### Desktop
| Home | ![screenshot](documentation/testing/lighthouse/lh-desktop-home.png) |  |  |
| --- | --- | --- | --- |
| ![screenshot](documentation/testing/lighthouse/lh-desktop-home-performance.png) | ![screenshot](documentation/testing/lighthouse/lh-desktop-home-access.png) | ![screenshot](documentation/testing/lighthouse/lh-desktop-home-bestpract.png) | ![screenshot](documentation/testing/lighthouse/lh-desktop-home-SEO.png) |
| issues mostly based on heroku | minor issues | issues based on cloudinary | issues based on trigging modals, and robots.txt |

| Popular News | ![screenshot](documentation/testing/lighthouse/lh-desktop-pop.png) |  |  |
| --- | --- | --- | --- |
| ![screenshot](documentation/testing/lighthouse/lh-desktop-pop-perfomance.png) | ![screenshot](documentation/testing/lighthouse/lh-desktop-pop-access.png) | ![screenshot](documentation/testing/lighthouse/lh-desktop-pop-bestpract.png) | ![screenshot](documentation/testing/lighthouse/lh-desktop-pop-SEO.png) |
| Same heroku, some minor about using jpg/png and not next gen | minor issues | issues based on cloudinary | issues based on trigging modals, and robots.txt |

| News Detail | ![screenshot](documentation/testing/lighthouse/lh-desktop-detail.png) |  |  |
| --- | --- | --- | --- |
| ![screenshot](documentation/testing/lighthouse/lh-desktop-detail-performance.png) | ![screenshot](documentation/testing/lighthouse/lh-desktop-detail-access.png) | ![screenshot](documentation/testing/lighthouse/lh-desktop-detail-bestpract.png) | ![screenshot](documentation/testing/lighthouse/lh-desktop-detail-SEO.png) |
| More of the same | minor issues, some i can not understand. Flags bootstrap elements, but ok score | same cloudinary https issues | issues based on trigging modals, and robots.txt |



## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Visual confirmation |
| --- | --- | --- | --- | --- |
| Home | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| Sign Up | | | | |
| | Click on Sign Up button | Open Sign up Modal | Pass | [![Sign Up Modal](https://i.gyazo.com/7eb6764de1329045c4446bbc6945d99d.gif)](https://gyazo.com/7eb6764de1329045c4446bbc6945d99d)|
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | ![Wrong Credentials](documentation/testing/def-wrong-up.png) |
| Sign In | | | | |
| | Click on the Login link | Open Sign in Modal | Pass | [![Sign in Modal](https://i.gyazo.com/120936924cbf351d80d245ea43ac794e.gif)](https://gyazo.com/120936924cbf351d80d245ea43ac794e) |
| | Enter valid credentials | Error message on wrong credentials | Pass | ![Wrong Credentials](documentation/testing/def-wrong-sign.png) |
| | Click Login button | Redirects user to home page and gets vissual confirmation | Pass | [![Login Confirmation](https://i.gyazo.com/315e0e227fb0ca80a63658d2c56954d8.gif)](https://gyazo.com/315e0e227fb0ca80a63658d2c56954d8) |
| Sign Out | | | | |
| | Click Logout button | Opens Sign out Modal, and gives visual feed back. | Pass | [![Sign out](https://i.gyazo.com/ff2647a1d752ec830dea64688a791d3c.gif)](https://gyazo.com/ff2647a1d752ec830dea64688a791d3c) |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Create News | | | | |
| | Click Create news | Opens Create News Modal Only for Signed In users | Pass | [![Open Create news](https://i.gyazo.com/ee6380cac65869b3d1fdc3564ff35c48.gif)](https://gyazo.com/ee6380cac65869b3d1fdc3564ff35c48) |
| | Fields need to have content  | A warning shows | Pass | ![Required Fields](documentation/testing/testing-create-required1.png) ![Required Fields](documentation/testing/testing-create-required2.png) |
| | Click Create News  | Creates news post and gives feedback on creation. Redirect to post | Pass | [![Create and redirect to News](https://i.gyazo.com/704d6e2dfee82f43641f752cd26027f0.gif)](https://gyazo.com/704d6e2dfee82f43641f752cd26027f0) |
| Edit News | | | | |
| | Click Edit | Edit button shows only on the USERS news posts | Pass | SCREEN |
| | Editing | All changes are made after klicking edit | Pass | SCREEN |
| | Delete | News posts gets deleted, with all its comments | Pass |  |
| | Delete Comment | The chosen comment gets deleted | Pass |  |


## User Story Testing

DONT FORGET THIS! 

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature01.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature02.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature03.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature04.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature05.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature06.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/feature07.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/feature08.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/feature09.png) |
| repeat for all remaining user stories | x |


## Database tests 
Creating News test. 

![Test of creating a post](documentation/testing/test-create-news-post.png) 
![Test of creating a post](documentation/testing/test-create-news-post-get.png) 

Login test. 

![Login test](documentation/testing/test-login-post-get.png) 

Vote system test.

![Vote systemt](documentation/testing/test-vote-post.png) 

## Bugs

During the development i encountered several bugs and problems, during development i seldome remember to take a screenshot, I just try to solve it, so if its just frontend glitches, or backend. 

![Edit Save and Delete](documentation/testing/edit-news-edit.png) 

Could not get the buttons to be next to each other. Could probably use more divs, but I feel there must be a better way Im missing. 

![Package errors](documentation/testing/test-cloudinary-error.png) 

I had way to many of these, things where installed, i could use them. But i just was not able to use it in my venv, reboots, new venv, nothing worked. But after an update of VScode solved it. Note to self, always update! 

![Form errors](documentation/testing/test-form-error.png)

Make sure you do your js the right way!

![Edit errors](documentation/testing/test-form-input.png) 

The function to prepopulate the edit Modal played tricks on me on several occations. Way to often it was just I who had placed a csrf_token wrong, or used the wrong post_form.as_p. 
The differance between using {%  or {{ was something i apparently found harder than i first thoght. 
This was also triggered by puting for loops and endfor in the wrong div.

### GitHub **Issues**

NEED TO MAKE THIS! 

An improved way to manage bugs is to use the built-in **Issues** tracker on your GitHub repository.
To access your Issues, click on the "Issues" tab at the top of your repository.
Alternatively, use this link: https://github.com/zakenaio/pp4-interesting2/issues

If using the Issues tracker for your bug management, you can simplify the documentation process.
Issues allow you to directly paste screenshots into the issue without having to first save the screenshot locally,
then uploading into your project.

You can add labels to your issues (`bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s).

Once you've sorted the issue, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following format:


**Fixed Bugs**

All previously closed/fixed bugs can be tracked [here](https://github.com/zakenaio/pp4-interesting2/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |


Any remaining open issues can be tracked [here](https://github.com/zakenaio/pp4-interesting2/issues).

| Bug | Status |
| --- | --- |
| [JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).](https://github.com/zakenaio/pp4-interesting2/issues/4) | Open |
| [Python `E501 line too long` (93 > 79 characters)](https://github.com/zakenaio/pp4-interesting2/issues/5) | Open |

## Unfixed Bugs

| Bug | Status |
| --- | --- |
| Using django links in some modals | Noticed that i had hardcoded links in some of my modals, after trying to fix the issue some of my modals broke, curtain faded but no modal was shown, i could not seem to resolve the issue at this point. | 
