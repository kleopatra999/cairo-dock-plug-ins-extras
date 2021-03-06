# This is a part of the external WebSearch applet for Cairo-Dock
# Author: Eduardo Mucelli Rezende Oliveira
# E-mail: edumucelli@gmail.com or eduardom@dcc.ufmg.br
#
# This module fetch results from Wikipedia - en.wikipedia.org

class Wikipedia < Engine

	attr_accessor :number_of_fetched_links

	def initialize
		self.name = self.class.to_s
		self.number_of_fetched_links = 100
		self.base_url = "http://en.wikipedia.org"
		self.query_url = "#{self.base_url}/w/index.php?title=Special:Search&search="				# parameter "limit" results per page
		super
	end
	
	# Fetch links from english Wikipedia. It is necessary to set user agent, or the connection is Forbidden (403)
	def retrieve_links(query, offset = 0)
		puts "Query #{self.query_url}#{query}&offset=#{offset}&limit=#{self.number_of_fetched_links}"
		wikipedia = Nokogiri::HTML(open("#{self.query_url}#{query}&offset=#{offset}&limit=#{self.number_of_fetched_links}", 'User-Agent' => 'ruby'))
		#self.stats = retrieve_webshots_result_wikipedia(wikipedia, query)
		(wikipedia/"ul[@class='mw-search-results']/li/div/a").each do |res|
			url = "#{self.base_url}#{res['href']}"
			description = res['title']
			self.links << Link.new(url, description)
		end
		self.links
	end

	def retrieve_webshots_result_wikipedia (wikipedia, query)
		total = wikipedia.at("div[@class='results-info']/ul/li/b").next.next.inner_text
		"Search for #{query} returned #{total} results"
	end
end
