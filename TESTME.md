# First considerations

As I said in the interview I am more skilled with Javascript and I am not a Python expert (yet ;-) ), 
so probably there are some things that could be better implemented. For instance, using generics to avoid have steps 
using an element and other using a list, I used a trick to transform into a list, but would be a better way.

Also my main focus was not into create a complete test suit covering perfectly the specification, it was just an 
implementation example.

# Decisions taken

Some steps could be reduced using a list, like `I should see an "<field>" in each result of response` in the
second scenario, this is done in this way only as example to reuse same step in same scenario.

I avoided check all detailed info returned by each category because of this 10.000 requests per day rate limit, but
we could do a step to do that.

I am managing just 1 response in the context because this is an example, for a more complex framework we could use
something more specific to can store more than 1 response in a generic way, this would be necessary for instance if we 
need recollect information from several places to do something.

I did not take care about use concurrency, but it is important in a framework.

I created before/after_all and before/after_scenario with a console output just to let you see where they are executed, 
here they are not necessary and console output should be avoided as much as we can to keep it readable.

There are steps where results field are have to be specified in feature to do it more generic/reusable but for this 
example it could be avoided to make it more readable.