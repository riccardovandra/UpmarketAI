prompt_swot_analysis = '''

Act as an expert marketing researcher.
Please create a SWOT analysis for the product below. Divide the text in paragraphs

Brand Description: {description_long}

Product Category: {product_category}

'''

prompt_strategy_goals = '''

I want you to act as a Digital Strategist. 
Help me create a digital marketing strategy, a concept for a creative campaign, a distribution plan, and provide suggestions for producing assets for the brand mentioned below.

Brand Description: {description_long}

Product Category: {product_category}

Goals: {campaign_goals}

Target: {target_audience}

'''

prompt_strategy_creation_high_level = '''

I want you to act as a Digital Strategist for me. 
I will provide you with market information, product details, and goals, and you will help me create a marketing strategy divided in the following way:

- Strategic Market Insights
- Strategy to achieve the goals
- Breaking down the goals into quarterly sub-goals
- Defining the target audience
- Defining the channel mix.

Brand Description: {description_long}

Product Category: {product_category}

Goals: {campaign_goals}

Target: {target_audience}

'''

prompt_why_mission_values = '''

I want you to act as a Brand Strategist. 

Based on the information below, help me define the following aspects of the brand. 
Make your best hypothesis about what they could be and why they might work.

Brand Why:

Mission / Brand Purpose:

Brand Values:

Brand Description: {description_long}

Product Category: {product_category}

Goals: {campaign_goals}

Target Audience: {target_audience}

Target Market: {target_market}
'''

prompt_strategy_phases_mapping = '''

I want you to act as a Digital Strategist. Help me define the stages of the marketing strategy based on the context discussed so far. 
Define a strategic plan that includes the following points (but is not limited to):

- Awareness phase to build awareness of the existence of the new product for the target audience.
- Consideration phase for users to consider the product within their reference brands before making a purchase.
- Conversion phase that encourages users to purchase the product.
- Retention phase that aims to bring existing customers back to the online store for recurring purchases.
- Planning of all stages.
- Indication of timelines for each phase, considering that the team will have 15 hours per week available.
- Division of activities into milestones and subtasks.

'''

prompt_marketing_objectives = '''

I want you to act as a Digital Strategist. 
Based on the previously defined marketing strategy, provide a detailed plan on how to achieve the business goal by the end of the year. 
Specify the quarterly objectives and explain the reasoning behind them.

Goals: {campaign_goals}
'''

prompt_marketing_plan = '''

I want you to act as a Digital Strategist. Based on the previously proposed strategy, create a comprehensive marketing plan, including (but not limited to):

Messaging:

Creative concepts for brand campaigns to be launched
Key Message
Claim
Distribution:

Potential traditional communication channels and media
Digital communication channels
Promotion:

Offers and incentives
Pricing:

Types of pricing to offer for individual products and/or bundles and why.

'''



