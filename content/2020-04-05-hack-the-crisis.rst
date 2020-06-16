Hack the Crisis: We Care!
#########################

:author: Ashwin Vishnu Mohanan
:date: 2020-04-05T20:38:02.657040
:modified: 2020-04-06T08:01:00
:slug: hack-the-crisis
:status: published
:summary: How we created project *We Care!* in this COVID-19 themed hackathon
:category: Tech Talk
:tags: software, open-source, covid-19

This weekend I was part of a great and amazing group of people working as a
team.  We where coders, designers, ideators, jack-of-all-trades, creators,
academics, researchers and doers. We all where part of even a bigger team in
the Hack for Crisis Initiative in Sweden https://www.hackthecrisis.se/

We came together from all different parts, working purely online, never worked
with each other before, We created *We Care!*, a website_ and an app
concept to keep you safe in crisis, that we submitted.

Here is a demo video_ and a screenshot from the live website_ of our solution.

.. raw:: html

   <div align='center'>
   <iframe id='ivplayer' width='100%' height='500px' src='https://invidious.snopyta.org/embed/rsBZuJEH1c0' style='border:none;'>
   </iframe>
   <iframe src="https://pixelfed.social/p/ashwinvis/152654039161638912/embed?caption=true&likes=false&layout=full" class="pixelfed__embed" style="max-width: 100%; border: 0" width="100%" allowfullscreen="allowfullscreen"></iframe><script async defer src="https://pixelfed.social/embed.js"></script>
   </div>


Nitty-gritty details
--------------------

The stack consists of a website (https://covidmap.se/) where the user can enter
symptom data as well as their postal code. This is then submitted to a Firebase
database, from which a Python application downloads the data submitted and
analyzes it in batches. The aggregated, anonymized results are then published
back to the database and can be viewed in the map.

The whole system was designed to function as follows:

.. image:: https://raw.githubusercontent.com/covidmap-sweden/welcome/master/architecture.jpg
   :width: 100%
   :class: m-image

A future improvement to this could either be to do the Python computation
directly in the Firebase Cloud Function and then submitted to the Firebase
database. Alternatively, to have the website publish its data to the Python
backend which in turn will post the outcome of the analysis to the Firebase
database. Either way, the user will get a response on their input.

The motivation for using postal codes is to get a granular overview of the
spread while still being within compliance of GDPR. Other suggestions have been
using Bank-ID as a user id form, but that combined with medical data would be a
GDPR issue we were not able to handle during the hackathon. We will also ensure
compliance with Swedish laws on research ethics, submitting for ethical review
if required so that collected data can be used for research purposes.

The backend alley
-----------------

On a personal note, I was working on getting the Python backend (written using
SQL Alchemy and Pandas) up and running. The essential pieces were present
thanks to the original Swiss team which open-sourced the project. The
enhancements we added on top of it were:

- smoothening installation process by adding a basic Python packaging
  ``setup.py``.
- post-processing scripts to calculate symptom risks with Pandas within the
  Python backend instead of doing it in the Vue.js frontend side
- a Flask microserver based REST API to reduce the data storage in the database
  and perform computation more frequently to keep the website up to date
- Creating a docker image of the application

Our intention was the deploy the backend in the cloud, but because of the time
constraint we were unable to achieve that target. For now the backend is
semi-automated. In due time, yes we can!

Did I mention our implementation was open-source_ as well!

The fight is far from over
--------------------------

If you want to help us please go in and test https://covidmap.se and self report
yourself and please share this post in your network if you want. You can also
visualize_ the aggregated results.

If you want to fast... go alone, if you want to go far go together. Thanks to
everyone in my team for a great experience. I loved working with you and being
part of this team.


.. _video: https://www.youtube.com/watch?v=rsBZuJEH1c0
.. _website: https://covidmap.se
.. _visualize: https://covidmap.se/visualize
.. _open-source: https://github.com/covidmap-sweden/
