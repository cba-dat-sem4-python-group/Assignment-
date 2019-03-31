[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cba-dat-sem4-python-group/Assignment-7/master?filepath=Assignment-7.ipynb)
# Assignment 7 Webscraping

## Part 1

* You must first retrieve the top 100 scoring posts from [https://old.reddit.com/top/?sort=top&t=all](https://old.reddit.com/top/?sort=top&t=all). You will need to walk through multiple pages, using the `next` button.
* Save the links in a list of `Post` objects. The `Post` object must contain:
    * The id of the post.
    * The title of the post.
    * The exact score of the post.
    * The subreddit the post was submitted to. 

## Part 2

What are the most popular subreddits in the top 100 posts?

* Find the frequency of all the subreddits in the 100 top posts. Store them in a dictionary where `subreddit=>frequency`.
* Sort the dictionary by descending value. 
* Plot the frequencies on a bar chart, where the `y`-axis is the frequency, and the `x`-axis is the subreddit name.

## Part 3

Search reddit using selenium.

Create a function that can retrieve the top `n` search results (posts) given a `search_term`.

```python
def search_reddit(search_term, n):
   pass
```

*remember to use `old.reddit.com` to aviod SPA.*

If you get stuck, you can check out our solution [here](https://github.com/Thomas-Rosenkrans-Vestergaard/thomas-kristoffer-assignment-solution).
