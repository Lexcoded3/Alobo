(function() {
    // Namespace
    window.AloboPortal = {
        init: function() {
            // Seed database if empty
            if (!localStorage.getItem('alobo_users')) {
                var defaultUsers = [
                    {
                        name: "Auma Florence",
                        email: "auma@gmail.com",
                        password: "password123",
                        ward: "Kengere"
                    }
                ];
                localStorage.setItem('alobo_users', JSON.stringify(defaultUsers));
            }
            if (!localStorage.getItem('alobo_requests')) {
                var defaultRequests = [
                    {
                        id: "SCE-26-401",
                        userEmail: "auma@gmail.com",
                        type: "Borehole Repair",
                        ward: "Kengere",
                        description: "The local borehole in Kengere Ward has been leaking and needs urgent repair to restore clean water access for 50+ households.",
                        phone: "+256 772 123456",
                        date: "2026-06-15",
                        status: "Resolved"
                    },
                    {
                        id: "SCE-26-405",
                        userEmail: "auma@gmail.com",
                        type: "Bursary Inquiry",
                        ward: "Kengere",
                        description: "Requesting details on the application process and deadlines for the Soroti City East Secondary School bursaries for the upcoming term.",
                        phone: "+256 772 123456",
                        date: "2026-07-01",
                        status: "In Progress"
                    }
                ];
                localStorage.setItem('alobo_requests', JSON.stringify(defaultRequests));
            }
            if (!localStorage.getItem('alobo_raised_amount')) {
                localStorage.setItem('alobo_raised_amount', '12750000');
            }
            if (!localStorage.getItem('alobo_donors_count')) {
                localStorage.setItem('alobo_donors_count', '1247');
            }
        },

        getUsers: function() {
            this.init();
            return JSON.parse(localStorage.getItem('alobo_users') || '[]');
        },

        getRequests: function() {
            this.init();
            return JSON.parse(localStorage.getItem('alobo_requests') || '[]');
        },

        getCurrentUser: function() {
            var email = localStorage.getItem('alobo_current_user');
            if (!email) return null;
            var users = this.getUsers();
            for (var i = 0; i < users.length; i++) {
                if (users[i].email === email) {
                    return users[i];
                }
            }
            return null;
        },

        register: function(name, email, password, ward) {
            var users = this.getUsers();
            // Check if user exists
            for (var i = 0; i < users.length; i++) {
                if (users[i].email.toLowerCase() === email.toLowerCase()) {
                    return { success: false, message: "An account with this email already exists." };
                }
            }
            var newUser = { name: name, email: email, password: password, ward: ward };
            users.push(newUser);
            localStorage.setItem('alobo_users', JSON.stringify(users));
            // Log in user
            localStorage.setItem('alobo_current_user', email);
            return { success: true };
        },

        login: function(email, password) {
            var users = this.getUsers();
            for (var i = 0; i < users.length; i++) {
                if (users[i].email.toLowerCase() === email.toLowerCase() && users[i].password === password) {
                    localStorage.setItem('alobo_current_user', users[i].email);
                    return { success: true };
                }
            }
            return { success: false, message: "Invalid email or password." };
        },

        logout: function() {
            localStorage.removeItem('alobo_current_user');
        },

        getUserRequests: function(email) {
            var allRequests = this.getRequests();
            return allRequests.filter(function(r) {
                return r.userEmail.toLowerCase() === email.toLowerCase();
            });
        },

        createRequest: function(userEmail, type, ward, description, phone) {
            var requests = this.getRequests();
            var randomId = Math.floor(100 + Math.random() * 900);
            var id = "SCE-26-" + randomId;
            var date = new Date().toISOString().split('T')[0];
            var newRequest = {
                id: id,
                userEmail: userEmail,
                type: type,
                ward: ward,
                description: description,
                phone: phone,
                date: date,
                status: "Under Review"
            };
            requests.unshift(newRequest); // Add to beginning
            localStorage.setItem('alobo_requests', JSON.stringify(requests));
            return { success: true, request: newRequest };
        },

        getCampaignStats: function() {
            this.init();
            return {
                goal: 50000000,
                raised: parseInt(localStorage.getItem('alobo_raised_amount') || '12750000'),
                donors: parseInt(localStorage.getItem('alobo_donors_count') || '1247'),
                days: 46
            };
        },

        addDonation: function(amount) {
            var stats = this.getCampaignStats();
            var newRaised = stats.raised + amount;
            var newDonors = stats.donors + 1;
            localStorage.setItem('alobo_raised_amount', newRaised.toString());
            localStorage.setItem('alobo_donors_count', newDonors.toString());
            return {
                goal: stats.goal,
                raised: newRaised,
                donors: newDonors,
                days: stats.days
            };
        }
    };
    window.AloboPortal.init();
})();
