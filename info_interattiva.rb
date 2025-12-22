#!/usr/bin/env ruby

require 'net/http'
require 'json'
require 'uri'

class GitHubInfo
  def initialize(username = 'mario Rossi')
    @username = username
    @url = "https://api.github.com/users/#{username}"
  end

  def get_info
    begin
      uri = URI(@url)
      response = Net::HTTP.get_response(uri)
      if response.code == '200'
        data = JSON.parse(response.body)
        {
          name: data['name'] || 'N/A',
          bio: data['bio'] || 'N/A',
          public_repos: data['public_repos'],
          followers: data['followers'],
          following: data['following']
        }
      else
        { error: "Utente non trovato o errore nella richiesta API" }
      end
    rescue => e
      { error: "Errore durante il recupero delle informazioni: #{e.message}" }
    end
  end
end

def mostra_menu
  puts "\n" + "="*50
  puts "Seleziona un'opzione:"
  puts "1. Nome"
  puts "2. Bio"
  puts "3. Numero di repository pubblici"
  puts "4. Numero di follower"
  puts "5. Numero di following"
  puts "6. Tutte le informazioni"
  puts "7. Esci"
  print "Inserisci il numero dell'opzione: "
end

def main
  puts "Benvenuto nell'applicazione informativa GitHub!"
  print "Inserisci il nome utente GitHub da cercare (default: mario Rossi): "
  input_username = gets.chomp.strip
  username = input_username.empty? ? 'mario Rossi' : input_username
  
  github_info = GitHubInfo.new(username)
  info = github_info.get_info
  
  if info[:error]
    puts info[:error]
    return
  end

  loop do
    mostra_menu
    scelta = gets.chomp.to_i

    case scelta
    when 1
      puts "\nNome: #{info[:name]}"
    when 2
      puts "\nBio: #{info[:bio]}"
    when 3
      puts "\nNumero di repository pubblici: #{info[:public_repos]}"
    when 4
      puts "\nNumero di follower: #{info[:followers]}"
    when 5
      puts "\nNumero di following: #{info[:following]}"
    when 6
      puts "\nTutte le informazioni:"
      puts "Nome: #{info[:name]}"
      puts "Bio: #{info[:bio]}"
      puts "Repository pubblici: #{info[:public_repos]}"
      puts "Follower: #{info[:followers]}"
      puts "Following: #{info[:following]}"
    when 7
      puts "\nGrazie per aver usato l'applicazione. Arrivederci!"
      break
    else
      puts "\nOpzione non valida. Riprova."
    end
    
    puts "\nPremi Invio per continuare..."
    gets
  end
end

main