import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { discoverUserLoad, addDislike, addLike } from "../../store/session";
import "./DiscoverPage.css";
import heart from "../../assets/heart.png";
import thumb from "../../assets/thumb.png";
import sadPanda from "../../assets/discover-placeholder.png";
import slider from "../../assets/slider.png";
import OpenModalButton from "../OpenModalButton";
import UpdatePreferencesForm from "../UpdatePreferencesModal";
import InformationModal from "../InformationModal";

export default function Discover() {
    const users = useSelector((state) => state.session.discoverUsers);
    const currentUser = useSelector((state) => state.session.user);
    const [loaded, setLoaded] = useState(false);
    const [userNumber, setUserNumber] = useState(0);
    const [errors, setErrors] = useState([]);
    const dispatch = useDispatch();

    let usersList = null;

    if (users) {
        usersList = Object.values(users);
    }

    useEffect(() => {
        dispatch(discoverUserLoad()).then(() => setLoaded(true));
    }, [dispatch, loaded]);

    if (!loaded) {
        return (
            <>
                <div className="discover-header-container">
                    <h1>Discover</h1>
                    <div className="discover-blurb">
                        <h4>Liking is boring.</h4>
                        <p>
                            Dislike Users to create Mismatches, and chat with
                            someone different for a change! Liking will remove
                            Users from your discover feed, but we won't let you
                            talk to them... yet!
                        </p>
                    </div>
                </div>
                <div className="discover-placeholder-div"></div>;
            </>
        );
    }

    if (!users) {
        return (
            <>
                <div className="discover-header-container">
                    <h1>Discover</h1>
                    <div className="discover-blurb">
                        <h4>Liking is boring.</h4>
                        <p>
                            Dislike Users to create Mismatches, and chat with
                            someone different for a change! Liking will remove
                            Users from your discover feed, but we won't let you
                            talk to them... yet!
                        </p>
                    </div>
                </div>
                <div className="discover-placeholder-div"></div>;
            </>
        );
    }

    if (usersList.length === 0) {
        return (
            <>
                <div className="discover-header-container">
                    <div className="pref-button-container">
                        <div className="pref-button-border">
                            <img
                                id="equalizer"
                                alt="pref-slider"
                                src={slider}
                            />
                            <OpenModalButton
                                buttonText="Update Preferences"
                                modalComponent={<UpdatePreferencesForm />}
                                className="preferences-open-button"
                            />
                        </div>
                    </div>
                    <h1>Discover</h1>
                    <div className="discover-blurb">
                        <h4>Liking is boring.</h4>
                        <p>
                            Dislike Users to create Mismatches, and chat with
                            someone different for a change! Liking will remove
                            Users from your discover feed, but we won't let you
                            talk to them... yet!
                        </p>
                    </div>
                </div>
                <div className="discover-page-placeholder">
                    <h2>
                        No more users match your preferences, adjust preferences
                        to see more.
                    </h2>
                    <img src={sadPanda} alt="alone-for-now" classname='alone-for-now'/>
                </div>
            </>
        );
    }

    let user = usersList[userNumber];
    const user1answers = currentUser.userAnswers.filter(
        (answer) => answer.answer !== null
    );
    const user2answers = user.userAnswers.filter(
        (answer) => answer.answer !== null
    );
    let sameQuestionCount = 0.0;
    let differentAnswerCount = 0.0;
    user1answers.forEach((user1answer) => {
        user2answers.forEach((user2answer) => {
            if (user1answer.questionId === user2answer.questionId) {
                sameQuestionCount += 1;
                if (user1answer.answer !== user2answer.answer) {
                    differentAnswerCount += 1;
                }
            }
        });
    });
    const mismatchPercentage = Math.floor(
        (differentAnswerCount / sameQuestionCount) * 100
    );

    const updateUserNumber = async () => {
        setLoaded(false);
        if (userNumber === usersList.length - 1) {
            setUserNumber(0);
        } else {
            setUserNumber(userNumber + 1);
        }
    };

    const handleDislike = async (e) => {
        e.preventDefault();
        const errors = [];
        const newDislike = await dispatch(addDislike(user.id));
        setLoaded(false);

        if (newDislike.errors) {
            newDislike.errors.forEach((error) => errors.push(error));
            setErrors(errors);
        }
    };

    const handleLike = async (e) => {
        e.preventDefault();
        const errors = [];
        const newLike = await dispatch(addLike(user.id));
        setLoaded(false);

        if (newLike.errors) {
            newLike.errors.forEach((error) => errors.push(error));
            setErrors(errors);
        }
    };

    if (!user) {
        return (
            <>
                <div className="discover-header-container">
                    <h1>Discover</h1>
                    <div className="discover-blurb">

                        <h4>Liking is boring.</h4>
                        <p>
                            Dislike Users to create Mismatches, and chat with
                            someone different for a change! Liking will remove
                            Users from your discover feed, but we won't let you
                            talk to them... yet!
                        </p>
                    </div>
                </div>
                <div className="discover-placeholder-div"></div>;
            </>
        );
    }

    return (
        <>
            <div className="discover-header-container">

                <div className="pref-button-container">
                    <div className="pref-button-border">
                        <img id="equalizer" alt="pref-slider" src={slider} />
                        <OpenModalButton
                            buttonText="Update Preferences"
                            modalComponent={<UpdatePreferencesForm />}
                            className="preferences-open-button"
                        />
                    </div>
                </div>
                <h1>Discover</h1>
                <div className="discover-blurb">
                    <h4>Liking is boring.</h4>
                    <p>
                        Dislike Users to create Mismatches, and chat with
                        someone different for a change! Liking will remove Users
                        from your discover feed, but we won't let you talk to
                        them... yet!
                    </p>
                </div>
            </div>
            <div className="discover-page-containter">
                <OpenModalButton
                    buttonText="?"
                    modalComponent={<InformationModal />}
                    className="preferences-open-button"
                />
                <ul>
                    {errors.map((error, idx) => (
                        <li key={idx}>{error}</li>
                    ))}
                </ul>
                <div className="discover-page-header">
                    <div className="discover-page-top">
                        <div className="discover-name-age">
                            <span id="user-name">
                                {user.firstName[0].toUpperCase() +
                                    user.firstName.slice(1)}{" "}
                                • {user.age}
                            </span>
                            <span>
                                {user.city}, {user.state}
                            </span>
                        </div>
                        <div className="buttons-container">
                            {!isNaN(mismatchPercentage) && (
                                <span className="percentage">
                                    {mismatchPercentage}%
                                </span>
                            )}
                            <button
                                className="dislike-button"
                                onMouseUp={handleDislike}
                            >
                                <img
                                    id="discover-button-icons"
                                    src={heart}
                                    alt="button-icon"
                                />
                                Dislike
                            </button>
                            <button
                                className="like-button"
                                onMouseUp={handleLike}
                            >
                                <img
                                    id="discover-button-icons"
                                    src={thumb}
                                    alt="button-icon"
                                />
                                Like
                            </button>
                            <button
                                onMouseUp={updateUserNumber}
                                className="skip-button"
                            >
                                Skip
                            </button>
                        </div>
                    </div>
                    <img
                        id="discover-image"
                        alt="discover-pic"
                        src={
                            user.userImages[0]
                                ? user.userImages[0].imageUrl
                                : "https://picsum.photos/256/256"
                        }
                    />
                </div>
                <div className="discover-info">
                    <h3 className="info-header">About {user.firstName}</h3>
                    <div className="info">
                        <span>Gender: {user.gender}</span>
                        <span>Preferred Genders: {user.preferredGenders}</span>
                        <span>Bio: {user.bio}</span>
                    </div>
                </div>
            </div>
        </>
    );
}
