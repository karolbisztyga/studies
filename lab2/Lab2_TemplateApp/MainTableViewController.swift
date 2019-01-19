//
//  MainTableViewController.swift
//  Lab2_TemplateApp
//
//  Created by Sebastian Ernst on 11/01/2019.
//  Copyright © 2019 KIS AGH. All rights reserved.
//

import UIKit
import NotificationBannerSwift
import Alamofire

class MainTableViewController: UITableViewController {
    
    var messages: [Message] = []
    let BASE_URL = "https://home.agh.edu.pl/~ernst/shoutbox.php"
    let SECRET = "ams2018"
    
    func loadDataFromServer(showAlert: Bool = false) {
        print("[*] reading data from server")
        let oldMessagesCount = self.messages.count
        self.messages.removeAll()
        self.tableView.reloadData()
        let url = self.BASE_URL + "?secret=" + self.SECRET
        // http get request
        AF.request(url).validate().responseJSON { response -> Void in
            
            switch response.result {
            case .success:
                print("[+] data loaded")
                let json = response.result.value as! NSDictionary
                let arr: NSArray = json["entries"] != nil ? json["entries"] as! NSArray : []
                //print(arr)
                let dateFormatter = DateFormatter()
                dateFormatter.dateFormat = "yyyy-MM-dd HH:mm:ss"
                for item in arr {
                    let dict = item as! NSDictionary
                    let name = dict["name"] as! String
                    let message = dict["message"] as! String
                    let time = dict["timestamp"] as! String
                    let date = dateFormatter.date(from: time)!
                    /*print("-----------")
                     print(name)
                     print(message)
                     print(date)*/
                    let msg = Message(_author: name, _time: date, _content: message)
                    self.messages.append(msg)
                }
                print("[+] data read properly, records: " + String(self.messages.count))
                // show notification banner
                if (showAlert) {
                    DispatchQueue.main.async {
                        let newMessagesCount = self.messages.count - oldMessagesCount
                        let bannerText = (newMessagesCount != 0) ? String(newMessagesCount) + " new messages" : "No new messages"
                        NotificationBanner(title: "Messages fetched", subtitle: bannerText, style: .success).show()
                    }
                }
                // sorting records by date
                self.messages = self.messages.sorted(by: { $0.time > $1.time })
                DispatchQueue.main.async {
                    self.tableView.reloadData()
                }
            case .failure(let error):
                print("[-] error: ")
                print(error)
            }
        }
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // load data from server
        self.loadDataFromServer()
    }
    
    @IBAction func refreshData(_ sender: Any) {
        // TODO: reload data from server
        self.loadDataFromServer(showAlert: true)
    }
    
    @IBAction func addMessage(_ sender: Any) {
        let alertController = UIAlertController(title: "New message", message: "Please state your name ad message", preferredStyle: .alert)
        alertController.addTextField(configurationHandler: { textField in
            textField.placeholder = "Your name"
        })
        alertController.addTextField(configurationHandler: { textField in
            textField.placeholder = "Your message"
        })
        let sendAction = UIAlertAction(title: "Send", style: .default, handler: { action in
            let name = alertController.textFields?[0].text!
            let message = alertController.textFields?[1].text!
            // sending data to the server
            let msg = Message(_author: name!, _time: Date(), _content: message!)
            self.sendMessage(message: msg)
        })
        alertController.addAction(sendAction)
        let cancelAction = UIAlertAction(title: "Cancel", style: .cancel, handler: { _ in })
        alertController.addAction(cancelAction)
        self.present(alertController, animated: true)
    }
    
    private func sendMessage(message: Message) {
        print("[*] sending data to server: '" + message.content + "', by: " + message.author)
        /*var request = URLRequest(url: URL(string: self.BASE_URL)!)
        request.setValue("application/x-www-form-urlencoded", forHTTPHeaderField: "Content-Type")
        request.httpMethod = "POST"*/
        var postString = "name=" + message.author
        postString += "&message=" + message.content
        postString += "&secret=" + self.SECRET
        var params = [
            "name": message.author,
            "message": message.content,
            "secret": self.SECRET
        ] as [String: Any]
        
        AF.request(self.BASE_URL + "?secret=" + self.SECRET,
            method: .post as HTTPMethod,
            parameters: params).validate().responseJSON { response -> Void in
            switch response.result {
            case .success:
                print("[+] data sent, response: ")
                print(response.result.value!)
                DispatchQueue.main.async {
                    self.loadDataFromServer()
                }
            case .failure(let err):
                print("[-] data send failure, error:")
                print(err)
            }
        }
        /*request.httpBody = postString.data(using: .utf8)
        let task = URLSession.shared.dataTask(with: request) { data, response, error in
            guard let data = data, error == nil else {                                                 // check for fundamental networking error
                print("[!] error=\(error)")
                return
            }
            
            if let httpStatus = response as? HTTPURLResponse, httpStatus.statusCode != 200 {           // check for http errors
                print("[-] statusCode should be 200, but is \(httpStatus.statusCode)")
                print("[-] response = \(response)")
            } else {
                print("[+] status code 200 - OK!")
                DispatchQueue.main.async {
                    self.loadDataFromServer()
                }
            }
            
            let responseString = String(data: data, encoding: .utf8)
            print("[*] responseString = \(responseString)")
        }
        task.resume()*/
    }
    
    // MARK: - Table view data source
    
    override func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // TODO: return actual number of messages instead of random value
        if section == 0 {
            return self.messages.count
        }
        else {
            return 0
        }
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "shoutboxItem", for: indexPath)
        if indexPath.section == 0 {
            // TODO: return actual data instead of random values
            let message = "This is a placeholder message " + String(indexPath.item)
            let sender = "Jane Doe"
            let timestamp = Date(timeIntervalSinceNow: -1.0 * Double(Int.random(in: 10...5000)))
            /*let components = Calendar.current.dateComponents([.hour, .minute, .second], from: timestamp, to: Date())
            let metadata = "by \(sender), \(components.hour!) hour(s), \(components.minute!) minute(s) and \(components.second!) second(s) ago"*/
            
            let msg = self.messages[indexPath.item] //Message(_author: sender, _time: timestamp, _content: message)
            cell.textLabel!.text = msg.getText()
            cell.detailTextLabel!.text = msg.getDetails()
        }
        return cell
    }
    
}
