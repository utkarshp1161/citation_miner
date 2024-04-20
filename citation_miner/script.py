from scholarly import scholarly
import time
from datetime import datetime



def get_affiliation_for_author(author_name):
    search_query = scholarly.search_author(author_name)
    try:
        author_profile = next(search_query, None)
        if author_profile:
            affiliation = author_profile.get('affiliation', 'NA')
            return affiliation
    except StopIteration:
        pass
    return 'NA'

def get_last_n_year_info(author_a, current_year, n=5):
    jj = 0
    publication_list, coauthors_info = [], {}
    for ii, publication in enumerate(author_a['publications']):
      try:
        pub_year = int(publication['bib']['pub_year']) 
      except:
        print(" the publication metadata doesnt have year info lets anyway add this in the list and substitue it with current year -- this is a hack")
        pub_year = current_year + n + 5
          
      if current_year - pub_year <= n:# this filters based on year
          jj+= 1
          print(f"accepted publication from year{pub_year}")
          print(f"{jj}th paper accepeted till now")
          if jj % 50 == 0:
              print("we have queried 50 papers in a row lets wait 30 seconds for avoid getting banned")
              time.sleep(30)  # Rate limiting

          publication_filled = scholarly.fill(publication)  # return dictionary

          print("accepting publication from year:********************************", pub_year)
          title = publication_filled['bib'].get('title', 'NA')
          authors = publication_filled['bib'].get('author', 'NA').split(' and ')
          citation = publication_filled['bib'].get('citation', 'NA')
          num_citations = publication_filled.get('num_citations', 'NA')
          author = publication_filled['bib'].get('author', 'NA')
          cites_per_year = publication_filled.get('cites_per_year', 'NA')
          journal = publication_filled['bib'].get('journal', 'NA')

          for author_name in authors:
              # Attempt to fetch affiliation for each coauthor
              affiliation = get_affiliation_for_author(author_name)

              # Track the most recent publication and affiliation for each coauthor
              if author_name not in coauthors_info or coauthors_info[author_name]['Last Publication Year'] < pub_year:
                  coauthors_info[author_name] = {
                      'Last Publication Year': pub_year,
                      'Last Publication Title': title,
                      'Affiliation': affiliation
                  }

          publication_list_i = [title, pub_year, citation, author, num_citations, cites_per_year, journal]
          publication_list.append(publication_list_i)
      else:
              print("Skipping publication from year:", pub_year)

    return publication_list, coauthors_info
